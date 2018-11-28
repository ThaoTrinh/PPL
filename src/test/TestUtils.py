import sys
import os
from antlr4 import Token, FileStream, CommonTokenStream
from antlr4.error.ErrorListener import ConsoleErrorListener  # ErrorListener
from MPLexer import MPLexer
from MPParser import MPParser
from ASTGeneration import ASTGeneration
from StaticCheck import StaticChecker
from StaticError import StaticError
from CodeGenerator import CodeGenerator
import subprocess
from lexererr import ErrorToken, UncloseString, IllegalEscape

if './main/mp/parser/' not in sys.path:
    sys.path.append('./main/mp/parser/')
if os.path.isdir('../target/main/mp/parser') and \
        '../target/main/mp/parser/' not in sys.path:
    sys.path.append('../target/main/mp/parser/')

JASMIN_JAR = "./external/jasmin.jar"
TEST_DIR = "./test/testcases/"
SOL_DIR = "./test/solutions/"
Lexer = MPLexer
Parser = MPParser

VERBOSE_MODE = True

if VERBOSE_MODE:
    tokens = open('../target/main/mp/parser/MP.tokens').readlines()
    token_map = {}
    for token in tokens:
        t = token[:-1].split('=')
        token_map[t[1]] = t[0]
    token_map['-1'] = '<EOF>'
    # print(token_map)


class TestUtil:
    @staticmethod
    def makeSource(inputStr, num):
        filename = TEST_DIR + str(num) + ".txt"
        file = open(filename, "w")
        file.write(inputStr)
        file.close()
        return FileStream(filename)


class TestLexer:
    @staticmethod
    def test(input, expect, num):
        global VERBOSE_MODE
        inputfile = TestUtil.makeSource(input, num)
        TestLexer.check(SOL_DIR, inputfile, num)
        dest = open(SOL_DIR + str(num) + ".txt", "r")
        line = dest.read()
        if VERBOSE_MODE:
            err = '*' if line != expect else '+'
            print("[{}] {} [{}] --> [{}] === [{}]".format(err, num,
                                                          input, line, expect))
            print('----------')
        return line == expect

    @staticmethod
    def check(soldir, inputfile, num):
        dest = open(soldir + "/" + str(num) + ".txt", "w")
        lexer = Lexer(inputfile)
        try:
            TestLexer.printLexeme(dest, lexer)
        except (ErrorToken, UncloseString, IllegalEscape) as err:
            dest.write(err.message)
        finally:
            dest.close()

    @staticmethod
    def printLexeme(dest, lexer):
        global VERBOSE_MODE
        tok = lexer.nextToken()
        if tok.type != Token.EOF:
            if VERBOSE_MODE:
                print(token_map[str(tok.type)] + ":: " + tok.text + " ;")
            dest.write(tok.text + ",")
            TestLexer.printLexeme(dest, lexer)
        else:
            dest.write("<EOF>")


class NewErrorListener(ConsoleErrorListener):
    INSTANCE = None

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise SyntaxException(
            "Error on line " +
            str(line) +
            " col " +
            str(column) +
            ": " +
            offendingSymbol.text)


NewErrorListener.INSTANCE = NewErrorListener()


class SyntaxException(Exception):
    def __init__(self, msg):
        self.message = msg


class TestParser:
    @staticmethod
    def createErrorListener():
        return NewErrorListener.INSTANCE

    @staticmethod
    def test(input, expect, num):
        inputfile = TestUtil.makeSource(input, num)
        TestParser.check(SOL_DIR, inputfile, num)
        dest = open(SOL_DIR + str(num) + ".txt", "r")
        line = dest.read()
        if VERBOSE_MODE:
            print('[{}] {} ================'
                  .format('*' if line != expect else '+', num))
        return line == expect

    @staticmethod
    def check(soldir, inputfile, num):
        dest = open(soldir + "/" + str(num) + ".txt", "w")
        lexer = Lexer(inputfile)
        listener = TestParser.createErrorListener()
        tokens = CommonTokenStream(lexer)

        if VERBOSE_MODE:
            print('[{}] -------------------'.format(num))
            # print token only
            # for i in range(tokens.getNumberOfOnChannelTokens()):
            #     print(i, token_map[str(tokens.LA(i + 1))])

        parser = Parser(tokens)
        parser.removeErrorListeners()
        parser.addErrorListener(listener)
        try:
            parser.program()
            if VERBOSE_MODE:
                print("successful")
            dest.write("successful")
        except SyntaxException as f:
            if VERBOSE_MODE:
                msg = f.message.split(':')[0].split(' ')
                line = int(msg[3])
                col = int(msg[5])
                error_line = open(TEST_DIR + '/' + str(num) + '.txt').read()
                error_line = error_line.split('\n')[line - 1]
                print(error_line)
                print('~' * (col) + '^')
                print(f.message)
            dest.write(f.message)
        except Exception as e:
            if VERBOSE_MODE:
                print(str(e))
            dest.write(str(e))
        finally:
            dest.close()


class TestAST:
    @staticmethod
    def test(input, expect, num):
        inputfile = TestUtil.makeSource(input, num)
        TestAST.check(SOL_DIR, inputfile, num)
        dest = open(SOL_DIR + str(num) + ".txt", "r")
        line = dest.read()
        if VERBOSE_MODE:
            err = '*' if line != expect else '+'
            print("[{}] {} [{}]\n-->[{}]\n===[{}]".format(
                err,
                num,
                input,
                line,
                expect)
            )
            print('----------')
        return line == expect

    @staticmethod
    def check(soldir, inputfile, num):
        dest = open(soldir + "/" + str(num) + ".txt", "w")
        lexer = Lexer(inputfile)
        tokens = CommonTokenStream(lexer)
        parser = Parser(tokens)
        tree = parser.program()
        asttree = ASTGeneration().visit(tree)
        dest.write(str(asttree))
        dest.close()


class TestChecker:
    @staticmethod
    def test(input, expect, num):
        if isinstance(input, str):
            inputfile = TestUtil.makeSource(input, num)
            lexer = Lexer(inputfile)
            tokens = CommonTokenStream(lexer)
            try:
                listener = TestParser.createErrorListener()
                parser = Parser(tokens)
                parser.removeErrorListeners()
                parser.addErrorListener(listener)
                tree = parser.program()
            except SyntaxException as f:
                if VERBOSE_MODE:
                    msg = f.message.split(':')[0].split(' ')
                    line = int(msg[3])
                    col = int(msg[5])
                    error_line = open(
                        TEST_DIR + '/' + str(num) + '.txt').read()
                    error_line = error_line.split('\n')[line - 1]
                    print('[*] {}'.format(num))
                    print(error_line)
                    print('~' * (col) + '^')
                    print(f.message)
                    raise f
            asttree = ASTGeneration().visit(tree)
        else:
            inputfile = TestUtil.makeSource(str(input), num)
            asttree = input
        TestChecker.check(SOL_DIR, asttree, num)
        dest = open(SOL_DIR + "/" + str(num) + ".txt", "r")
        line = dest.read()
        if VERBOSE_MODE:
            err = '*' if line != expect else '+'
            print("[{}] {} [{}]\n-->[{}]\n-->[{}]\n===[{}]".format(
                err,
                num,
                input,
                str(asttree),
                line,
                expect)
            )
            print('----------')
        return line == expect

    @staticmethod
    def check(soldir, asttree, num):
        dest = open(soldir + "/" + str(num) + ".txt", "w")
        checker = StaticChecker(asttree)
        try:
            res = checker.check()
            # dest.write(str(list(res)))
            dest.write(','.join(str(x) for x in list(res)))
        except StaticError as e:
            dest.write(str(e))
        finally:
            dest.close()


class TestCodeGen():
    @staticmethod
    def test(input, expect, num):
        if isinstance(input, str):
            inputfile = TestUtil.makeSource(input, num)
            lexer = Lexer(inputfile)
            tokens = CommonTokenStream(lexer)
            try:
                listener = TestParser.createErrorListener()
                parser = Parser(tokens)
                parser.removeErrorListeners()
                parser.addErrorListener(listener)
                tree = parser.program()
            except SyntaxException as f:
                if VERBOSE_MODE:
                    msg = f.message.split(':')[0].split(' ')
                    line = int(msg[3])
                    col = int(msg[5])
                    error_line = open(
                        TEST_DIR + '/' + str(num) + '.txt').read()
                    error_line = error_line.split('\n')[line - 1]
                    print('[*] {}'.format(num))
                    print(error_line)
                    print('~' * (col) + '^')
                    print(f.message)
                    raise f
            asttree = ASTGeneration().visit(tree)
        else:
            inputfile = TestUtil.makeSource(str(input), num)
            asttree = input

        checker = StaticChecker(asttree)
        try:
            checker.check()
        except StaticError as e:
            if VERBOSE_MODE:
                print('[*] {} [{}]\n-->[{}]'.format(
                    num, inputfile, str(asttree)))
                print('*' * 10, '{}'.format(num), str(e))
                raise e

        TestCodeGen.check(SOL_DIR, asttree, num)

        dest = open(SOL_DIR + "/" + str(num) + ".txt", "r")
        line = dest.read()
        if VERBOSE_MODE:
            err = '*' if line != expect else '+'
            print('''[{}] {} [{}]
-->[{}]
-->[
{}
]
-->[{}]
===[{}]'''.format(
                err,
                num,
                input,
                str(asttree),
                open(SOL_DIR + '/' + str(num) + '/' + 'MPClass.j').read(),
                line,
                expect)
            )
            print('----------')
        return line == expect

    @staticmethod
    def check(soldir, asttree, num):
        codeGen = CodeGenerator()
        path = soldir + "/" + str(num)
        if not os.path.isdir(path):
            os.mkdir(path)
        f = open(soldir + "/" + str(num) + ".txt", "w")
        try:
            codeGen.gen(asttree, path)

            subprocess.call(
                "java  -jar " + JASMIN_JAR + " " + path + "/MPClass.j",
                shell=True,
                stderr=subprocess.STDOUT
            )

            subprocess.run(
                "java -cp ./lib:. MPClass",
                shell=True,
                stdout=f,
                timeout=10
            )
        except StaticError as e:
            f.write(str(e))
        except subprocess.TimeoutExpired:
            f.write("Time out\n")
        except subprocess.CalledProcessError as e:
            raise RuntimeError("command '{}' return with error (code {}): {}"
                               .format(e.cmd, e.returncode, e.output))
        finally:
            f.close()