# Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2A")
        buf.write("\u0243\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\t")
        buf.write("U\4V\tV\4W\tW\4X\tX\4Y\tY\4Z\tZ\4[\t[\3\2\3\2\3\3\3\3")
        buf.write("\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\7\3\b\3\b\3\t\3\t\3")
        buf.write("\t\3\n\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17")
        buf.write("\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24")
        buf.write("\3\25\3\25\3\25\3\26\3\26\3\26\3\27\3\27\3\27\3\27\7\27")
        buf.write("\u00eb\n\27\f\27\16\27\u00ee\13\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\30\3\30\7\30\u00f7\n\30\f\30\16\30\u00fa\13\30")
        buf.write("\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\7\31\u0104\n")
        buf.write("\31\f\31\16\31\u0107\13\31\3\31\7\31\u010a\n\31\f\31\16")
        buf.write("\31\u010d\13\31\3\31\3\31\3\31\3\31\3\32\3\32\5\32\u0115")
        buf.write("\n\32\3\32\6\32\u0118\n\32\r\32\16\32\u0119\3\33\3\33")
        buf.write("\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3")
        buf.write("\"\3\"\3#\3#\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*")
        buf.write("\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61")
        buf.write("\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\5\65\u0152\n")
        buf.write("\65\3\66\3\66\3\66\3\66\3\67\3\67\3\67\3\67\3\67\3\67")
        buf.write("\3\67\3\67\3\67\38\38\38\38\38\38\38\38\38\38\39\39\3")
        buf.write("9\39\39\39\3:\3:\3:\3:\3:\3:\3:\3:\3:\3;\3;\3;\3;\3<\3")
        buf.write("<\3<\3=\3=\3=\3=\3=\3=\3=\3>\3>\3>\3?\3?\3?\3@\3@\3@\3")
        buf.write("@\3@\3A\3A\3A\3A\3A\3B\3B\3B\3B\3B\3B\3B\3C\3C\3C\3C\3")
        buf.write("C\3C\3D\3D\3D\3D\3D\3D\3E\3E\3E\3E\3F\3F\3F\3F\3F\3G\3")
        buf.write("G\3G\3G\3G\3G\3H\3H\3H\3H\3H\3H\3I\3I\3I\3J\3J\3J\3J\3")
        buf.write("J\3J\3J\3J\3K\3K\3K\3K\3K\3K\3K\3K\3L\3L\3L\3L\3L\3M\3")
        buf.write("M\3M\3M\3M\3M\3M\3N\3N\3N\3N\3O\3O\3O\3O\3P\3P\3P\3Q\3")
        buf.write("Q\3Q\3Q\3R\3R\3R\3R\3S\3S\3S\3S\3S\3T\6T\u01f8\nT\rT\16")
        buf.write("T\u01f9\3U\6U\u01fd\nU\rU\16U\u01fe\3U\3U\7U\u0203\nU")
        buf.write("\fU\16U\u0206\13U\3U\5U\u0209\nU\5U\u020b\nU\3U\5U\u020e")
        buf.write("\nU\3U\3U\6U\u0212\nU\rU\16U\u0213\3U\5U\u0217\nU\3U\3")
        buf.write("U\5U\u021b\nU\3V\3V\3V\3V\3W\5W\u0222\nW\3W\7W\u0225\n")
        buf.write("W\fW\16W\u0228\13W\3X\6X\u022b\nX\rX\16X\u022c\3X\3X\3")
        buf.write("Y\3Y\3Y\3Y\7Y\u0235\nY\fY\16Y\u0238\13Y\3Y\3Y\3Z\3Z\3")
        buf.write("Z\3Z\3Z\3[\3[\3[\5\u00ec\u00f8\u0105\2\\\3\3\5\4\7\5\t")
        buf.write("\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20")
        buf.write("\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\2\65")
        buf.write("\2\67\29\2;\2=\2?\2A\2C\2E\2G\2I\2K\2M\2O\2Q\2S\2U\2W")
        buf.write("\2Y\2[\2]\2_\2a\2c\2e\2g\2i\33k\34m\35o\36q\37s u!w\"")
        buf.write("y#{$}%\177&\u0081\'\u0083(\u0085)\u0087*\u0089+\u008b")
        buf.write(",\u008d-\u008f.\u0091/\u0093\60\u0095\61\u0097\62\u0099")
        buf.write("\63\u009b\64\u009d\65\u009f\66\u00a1\67\u00a38\u00a59")
        buf.write("\u00a7:\u00a9;\u00ab<\u00ad=\u00af>\u00b1?\u00b3@\u00b5")
        buf.write("A\3\2$\3\2\17\17\3\2\f\f\3\2\62;\4\2CCcc\4\2DDdd\4\2E")
        buf.write("Eee\4\2FFff\4\2GGgg\4\2HHhh\4\2IIii\4\2JJjj\4\2KKkk\4")
        buf.write("\2LLll\4\2MMmm\4\2NNnn\4\2OOoo\4\2PPpp\4\2QQqq\4\2RRr")
        buf.write("r\4\2SSss\4\2TTtt\4\2UUuu\4\2VVvv\4\2WWww\4\2XXxx\4\2")
        buf.write("YYyy\4\2ZZzz\4\2[[{{\4\2\\\\||\5\2C\\aac|\6\2\62;C\\a")
        buf.write("ac|\5\2\13\f\17\17\"\"\n\2$$))^^ddhhppttvv\7\2\n\f\16")
        buf.write("\17$$))^^\2\u023c\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2")
        buf.write("\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2")
        buf.write("\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2")
        buf.write("\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2i\3\2\2\2\2k")
        buf.write("\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2")
        buf.write("u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2")
        buf.write("\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085")
        buf.write("\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2")
        buf.write("\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093")
        buf.write("\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2\2\2\u0099\3\2\2")
        buf.write("\2\2\u009b\3\2\2\2\2\u009d\3\2\2\2\2\u009f\3\2\2\2\2\u00a1")
        buf.write("\3\2\2\2\2\u00a3\3\2\2\2\2\u00a5\3\2\2\2\2\u00a7\3\2\2")
        buf.write("\2\2\u00a9\3\2\2\2\2\u00ab\3\2\2\2\2\u00ad\3\2\2\2\2\u00af")
        buf.write("\3\2\2\2\2\u00b1\3\2\2\2\2\u00b3\3\2\2\2\2\u00b5\3\2\2")
        buf.write("\2\3\u00b7\3\2\2\2\5\u00b9\3\2\2\2\7\u00bb\3\2\2\2\t\u00bd")
        buf.write("\3\2\2\2\13\u00bf\3\2\2\2\r\u00c1\3\2\2\2\17\u00c4\3\2")
        buf.write("\2\2\21\u00c6\3\2\2\2\23\u00c9\3\2\2\2\25\u00cc\3\2\2")
        buf.write("\2\27\u00ce\3\2\2\2\31\u00d0\3\2\2\2\33\u00d2\3\2\2\2")
        buf.write("\35\u00d4\3\2\2\2\37\u00d6\3\2\2\2!\u00d8\3\2\2\2#\u00da")
        buf.write("\3\2\2\2%\u00dc\3\2\2\2\'\u00de\3\2\2\2)\u00e0\3\2\2\2")
        buf.write("+\u00e3\3\2\2\2-\u00e6\3\2\2\2/\u00f4\3\2\2\2\61\u00ff")
        buf.write("\3\2\2\2\63\u0112\3\2\2\2\65\u011b\3\2\2\2\67\u011d\3")
        buf.write("\2\2\29\u011f\3\2\2\2;\u0121\3\2\2\2=\u0123\3\2\2\2?\u0125")
        buf.write("\3\2\2\2A\u0127\3\2\2\2C\u0129\3\2\2\2E\u012b\3\2\2\2")
        buf.write("G\u012d\3\2\2\2I\u012f\3\2\2\2K\u0131\3\2\2\2M\u0133\3")
        buf.write("\2\2\2O\u0135\3\2\2\2Q\u0137\3\2\2\2S\u0139\3\2\2\2U\u013b")
        buf.write("\3\2\2\2W\u013d\3\2\2\2Y\u013f\3\2\2\2[\u0141\3\2\2\2")
        buf.write("]\u0143\3\2\2\2_\u0145\3\2\2\2a\u0147\3\2\2\2c\u0149\3")
        buf.write("\2\2\2e\u014b\3\2\2\2g\u014d\3\2\2\2i\u0151\3\2\2\2k\u0153")
        buf.write("\3\2\2\2m\u0157\3\2\2\2o\u0160\3\2\2\2q\u016a\3\2\2\2")
        buf.write("s\u0170\3\2\2\2u\u0179\3\2\2\2w\u017d\3\2\2\2y\u0180\3")
        buf.write("\2\2\2{\u0187\3\2\2\2}\u018a\3\2\2\2\177\u018d\3\2\2\2")
        buf.write("\u0081\u0192\3\2\2\2\u0083\u0197\3\2\2\2\u0085\u019e\3")
        buf.write("\2\2\2\u0087\u01a4\3\2\2\2\u0089\u01aa\3\2\2\2\u008b\u01ae")
        buf.write("\3\2\2\2\u008d\u01b3\3\2\2\2\u008f\u01b9\3\2\2\2\u0091")
        buf.write("\u01bf\3\2\2\2\u0093\u01c2\3\2\2\2\u0095\u01ca\3\2\2\2")
        buf.write("\u0097\u01d2\3\2\2\2\u0099\u01d7\3\2\2\2\u009b\u01de\3")
        buf.write("\2\2\2\u009d\u01e2\3\2\2\2\u009f\u01e6\3\2\2\2\u00a1\u01e9")
        buf.write("\3\2\2\2\u00a3\u01ed\3\2\2\2\u00a5\u01f1\3\2\2\2\u00a7")
        buf.write("\u01f7\3\2\2\2\u00a9\u021a\3\2\2\2\u00ab\u021c\3\2\2\2")
        buf.write("\u00ad\u0221\3\2\2\2\u00af\u022a\3\2\2\2\u00b1\u0230\3")
        buf.write("\2\2\2\u00b3\u023b\3\2\2\2\u00b5\u0240\3\2\2\2\u00b7\u00b8")
        buf.write("\7-\2\2\u00b8\4\3\2\2\2\u00b9\u00ba\7/\2\2\u00ba\6\3\2")
        buf.write("\2\2\u00bb\u00bc\7,\2\2\u00bc\b\3\2\2\2\u00bd\u00be\7")
        buf.write("\61\2\2\u00be\n\3\2\2\2\u00bf\u00c0\7?\2\2\u00c0\f\3\2")
        buf.write("\2\2\u00c1\u00c2\7>\2\2\u00c2\u00c3\7@\2\2\u00c3\16\3")
        buf.write("\2\2\2\u00c4\u00c5\7>\2\2\u00c5\20\3\2\2\2\u00c6\u00c7")
        buf.write("\7>\2\2\u00c7\u00c8\7?\2\2\u00c8\22\3\2\2\2\u00c9\u00ca")
        buf.write("\7@\2\2\u00ca\u00cb\7?\2\2\u00cb\24\3\2\2\2\u00cc\u00cd")
        buf.write("\7@\2\2\u00cd\26\3\2\2\2\u00ce\u00cf\7*\2\2\u00cf\30\3")
        buf.write("\2\2\2\u00d0\u00d1\7+\2\2\u00d1\32\3\2\2\2\u00d2\u00d3")
        buf.write("\7]\2\2\u00d3\34\3\2\2\2\u00d4\u00d5\7_\2\2\u00d5\36\3")
        buf.write("\2\2\2\u00d6\u00d7\7}\2\2\u00d7 \3\2\2\2\u00d8\u00d9\7")
        buf.write("\177\2\2\u00d9\"\3\2\2\2\u00da\u00db\7=\2\2\u00db$\3\2")
        buf.write("\2\2\u00dc\u00dd\7<\2\2\u00dd&\3\2\2\2\u00de\u00df\7.")
        buf.write("\2\2\u00df(\3\2\2\2\u00e0\u00e1\7\60\2\2\u00e1\u00e2\7")
        buf.write("\60\2\2\u00e2*\3\2\2\2\u00e3\u00e4\7<\2\2\u00e4\u00e5")
        buf.write("\7?\2\2\u00e5,\3\2\2\2\u00e6\u00e7\7*\2\2\u00e7\u00e8")
        buf.write("\7,\2\2\u00e8\u00ec\3\2\2\2\u00e9\u00eb\13\2\2\2\u00ea")
        buf.write("\u00e9\3\2\2\2\u00eb\u00ee\3\2\2\2\u00ec\u00ed\3\2\2\2")
        buf.write("\u00ec\u00ea\3\2\2\2\u00ed\u00ef\3\2\2\2\u00ee\u00ec\3")
        buf.write("\2\2\2\u00ef\u00f0\7,\2\2\u00f0\u00f1\7+\2\2\u00f1\u00f2")
        buf.write("\3\2\2\2\u00f2\u00f3\b\27\2\2\u00f3.\3\2\2\2\u00f4\u00f8")
        buf.write("\7}\2\2\u00f5\u00f7\13\2\2\2\u00f6\u00f5\3\2\2\2\u00f7")
        buf.write("\u00fa\3\2\2\2\u00f8\u00f9\3\2\2\2\u00f8\u00f6\3\2\2\2")
        buf.write("\u00f9\u00fb\3\2\2\2\u00fa\u00f8\3\2\2\2\u00fb\u00fc\7")
        buf.write("\177\2\2\u00fc\u00fd\3\2\2\2\u00fd\u00fe\b\30\2\2\u00fe")
        buf.write("\60\3\2\2\2\u00ff\u0100\7\61\2\2\u0100\u0101\7\61\2\2")
        buf.write("\u0101\u0105\3\2\2\2\u0102\u0104\13\2\2\2\u0103\u0102")
        buf.write("\3\2\2\2\u0104\u0107\3\2\2\2\u0105\u0106\3\2\2\2\u0105")
        buf.write("\u0103\3\2\2\2\u0106\u010b\3\2\2\2\u0107\u0105\3\2\2\2")
        buf.write("\u0108\u010a\t\2\2\2\u0109\u0108\3\2\2\2\u010a\u010d\3")
        buf.write("\2\2\2\u010b\u0109\3\2\2\2\u010b\u010c\3\2\2\2\u010c\u010e")
        buf.write("\3\2\2\2\u010d\u010b\3\2\2\2\u010e\u010f\t\3\2\2\u010f")
        buf.write("\u0110\3\2\2\2\u0110\u0111\b\31\2\2\u0111\62\3\2\2\2\u0112")
        buf.write("\u0114\5=\37\2\u0113\u0115\7/\2\2\u0114\u0113\3\2\2\2")
        buf.write("\u0114\u0115\3\2\2\2\u0115\u0117\3\2\2\2\u0116\u0118\t")
        buf.write("\4\2\2\u0117\u0116\3\2\2\2\u0118\u0119\3\2\2\2\u0119\u0117")
        buf.write("\3\2\2\2\u0119\u011a\3\2\2\2\u011a\64\3\2\2\2\u011b\u011c")
        buf.write("\t\5\2\2\u011c\66\3\2\2\2\u011d\u011e\t\6\2\2\u011e8\3")
        buf.write("\2\2\2\u011f\u0120\t\7\2\2\u0120:\3\2\2\2\u0121\u0122")
        buf.write("\t\b\2\2\u0122<\3\2\2\2\u0123\u0124\t\t\2\2\u0124>\3\2")
        buf.write("\2\2\u0125\u0126\t\n\2\2\u0126@\3\2\2\2\u0127\u0128\t")
        buf.write("\13\2\2\u0128B\3\2\2\2\u0129\u012a\t\f\2\2\u012aD\3\2")
        buf.write("\2\2\u012b\u012c\t\r\2\2\u012cF\3\2\2\2\u012d\u012e\t")
        buf.write("\16\2\2\u012eH\3\2\2\2\u012f\u0130\t\17\2\2\u0130J\3\2")
        buf.write("\2\2\u0131\u0132\t\20\2\2\u0132L\3\2\2\2\u0133\u0134\t")
        buf.write("\21\2\2\u0134N\3\2\2\2\u0135\u0136\t\22\2\2\u0136P\3\2")
        buf.write("\2\2\u0137\u0138\t\23\2\2\u0138R\3\2\2\2\u0139\u013a\t")
        buf.write("\24\2\2\u013aT\3\2\2\2\u013b\u013c\t\25\2\2\u013cV\3\2")
        buf.write("\2\2\u013d\u013e\t\26\2\2\u013eX\3\2\2\2\u013f\u0140\t")
        buf.write("\27\2\2\u0140Z\3\2\2\2\u0141\u0142\t\30\2\2\u0142\\\3")
        buf.write("\2\2\2\u0143\u0144\t\31\2\2\u0144^\3\2\2\2\u0145\u0146")
        buf.write("\t\32\2\2\u0146`\3\2\2\2\u0147\u0148\t\33\2\2\u0148b\3")
        buf.write("\2\2\2\u0149\u014a\t\34\2\2\u014ad\3\2\2\2\u014b\u014c")
        buf.write("\t\35\2\2\u014cf\3\2\2\2\u014d\u014e\t\36\2\2\u014eh\3")
        buf.write("\2\2\2\u014f\u0152\5\u008bF\2\u0150\u0152\5\u008dG\2\u0151")
        buf.write("\u014f\3\2\2\2\u0151\u0150\3\2\2\2\u0152j\3\2\2\2\u0153")
        buf.write("\u0154\5_\60\2\u0154\u0155\5\65\33\2\u0155\u0156\5W,\2")
        buf.write("\u0156l\3\2\2\2\u0157\u0158\5? \2\u0158\u0159\5]/\2\u0159")
        buf.write("\u015a\5O(\2\u015a\u015b\59\35\2\u015b\u015c\5[.\2\u015c")
        buf.write("\u015d\5E#\2\u015d\u015e\5Q)\2\u015e\u015f\5O(\2\u015f")
        buf.write("n\3\2\2\2\u0160\u0161\5S*\2\u0161\u0162\5W,\2\u0162\u0163")
        buf.write("\5Q)\2\u0163\u0164\59\35\2\u0164\u0165\5=\37\2\u0165\u0166")
        buf.write("\5;\36\2\u0166\u0167\5]/\2\u0167\u0168\5W,\2\u0168\u0169")
        buf.write("\5=\37\2\u0169p\3\2\2\2\u016a\u016b\5\67\34\2\u016b\u016c")
        buf.write("\5W,\2\u016c\u016d\5=\37\2\u016d\u016e\5\65\33\2\u016e")
        buf.write("\u016f\5I%\2\u016fr\3\2\2\2\u0170\u0171\59\35\2\u0171")
        buf.write("\u0172\5Q)\2\u0172\u0173\5O(\2\u0173\u0174\5[.\2\u0174")
        buf.write("\u0175\5E#\2\u0175\u0176\5O(\2\u0176\u0177\5]/\2\u0177")
        buf.write("\u0178\5=\37\2\u0178t\3\2\2\2\u0179\u017a\5? \2\u017a")
        buf.write("\u017b\5Q)\2\u017b\u017c\5W,\2\u017cv\3\2\2\2\u017d\u017e")
        buf.write("\5[.\2\u017e\u017f\5Q)\2\u017fx\3\2\2\2\u0180\u0181\5")
        buf.write(";\36\2\u0181\u0182\5Q)\2\u0182\u0183\5a\61\2\u0183\u0184")
        buf.write("\5O(\2\u0184\u0185\5[.\2\u0185\u0186\5Q)\2\u0186z\3\2")
        buf.write("\2\2\u0187\u0188\5;\36\2\u0188\u0189\5Q)\2\u0189|\3\2")
        buf.write("\2\2\u018a\u018b\5E#\2\u018b\u018c\5? \2\u018c~\3\2\2")
        buf.write("\2\u018d\u018e\5[.\2\u018e\u018f\5C\"\2\u018f\u0190\5")
        buf.write("=\37\2\u0190\u0191\5O(\2\u0191\u0080\3\2\2\2\u0192\u0193")
        buf.write("\5=\37\2\u0193\u0194\5K&\2\u0194\u0195\5Y-\2\u0195\u0196")
        buf.write("\5=\37\2\u0196\u0082\3\2\2\2\u0197\u0198\5W,\2\u0198\u0199")
        buf.write("\5=\37\2\u0199\u019a\5[.\2\u019a\u019b\5]/\2\u019b\u019c")
        buf.write("\5W,\2\u019c\u019d\5O(\2\u019d\u0084\3\2\2\2\u019e\u019f")
        buf.write("\5a\61\2\u019f\u01a0\5C\"\2\u01a0\u01a1\5E#\2\u01a1\u01a2")
        buf.write("\5K&\2\u01a2\u01a3\5=\37\2\u01a3\u0086\3\2\2\2\u01a4\u01a5")
        buf.write("\5\67\34\2\u01a5\u01a6\5=\37\2\u01a6\u01a7\5A!\2\u01a7")
        buf.write("\u01a8\5E#\2\u01a8\u01a9\5O(\2\u01a9\u0088\3\2\2\2\u01aa")
        buf.write("\u01ab\5=\37\2\u01ab\u01ac\5O(\2\u01ac\u01ad\5;\36\2\u01ad")
        buf.write("\u008a\3\2\2\2\u01ae\u01af\5[.\2\u01af\u01b0\5W,\2\u01b0")
        buf.write("\u01b1\5]/\2\u01b1\u01b2\5=\37\2\u01b2\u008c\3\2\2\2\u01b3")
        buf.write("\u01b4\5? \2\u01b4\u01b5\5\65\33\2\u01b5\u01b6\5K&\2\u01b6")
        buf.write("\u01b7\5Y-\2\u01b7\u01b8\5=\37\2\u01b8\u008e\3\2\2\2\u01b9")
        buf.write("\u01ba\5\65\33\2\u01ba\u01bb\5W,\2\u01bb\u01bc\5W,\2\u01bc")
        buf.write("\u01bd\5\65\33\2\u01bd\u01be\5e\63\2\u01be\u0090\3\2\2")
        buf.write("\2\u01bf\u01c0\5Q)\2\u01c0\u01c1\5? \2\u01c1\u0092\3\2")
        buf.write("\2\2\u01c2\u01c3\5E#\2\u01c3\u01c4\5O(\2\u01c4\u01c5\5")
        buf.write("[.\2\u01c5\u01c6\5=\37\2\u01c6\u01c7\5A!\2\u01c7\u01c8")
        buf.write("\5=\37\2\u01c8\u01c9\5W,\2\u01c9\u0094\3\2\2\2\u01ca\u01cb")
        buf.write("\5\67\34\2\u01cb\u01cc\5Q)\2\u01cc\u01cd\5Q)\2\u01cd\u01ce")
        buf.write("\5K&\2\u01ce\u01cf\5=\37\2\u01cf\u01d0\5\65\33\2\u01d0")
        buf.write("\u01d1\5O(\2\u01d1\u0096\3\2\2\2\u01d2\u01d3\5W,\2\u01d3")
        buf.write("\u01d4\5=\37\2\u01d4\u01d5\5\65\33\2\u01d5\u01d6\5K&\2")
        buf.write("\u01d6\u0098\3\2\2\2\u01d7\u01d8\5Y-\2\u01d8\u01d9\5[")
        buf.write(".\2\u01d9\u01da\5W,\2\u01da\u01db\5E#\2\u01db\u01dc\5")
        buf.write("O(\2\u01dc\u01dd\5A!\2\u01dd\u009a\3\2\2\2\u01de\u01df")
        buf.write("\5O(\2\u01df\u01e0\5Q)\2\u01e0\u01e1\5[.\2\u01e1\u009c")
        buf.write("\3\2\2\2\u01e2\u01e3\5\65\33\2\u01e3\u01e4\5O(\2\u01e4")
        buf.write("\u01e5\5;\36\2\u01e5\u009e\3\2\2\2\u01e6\u01e7\5Q)\2\u01e7")
        buf.write("\u01e8\5W,\2\u01e8\u00a0\3\2\2\2\u01e9\u01ea\5;\36\2\u01ea")
        buf.write("\u01eb\5E#\2\u01eb\u01ec\5_\60\2\u01ec\u00a2\3\2\2\2\u01ed")
        buf.write("\u01ee\5M\'\2\u01ee\u01ef\5Q)\2\u01ef\u01f0\5;\36\2\u01f0")
        buf.write("\u00a4\3\2\2\2\u01f1\u01f2\5a\61\2\u01f2\u01f3\5E#\2\u01f3")
        buf.write("\u01f4\5[.\2\u01f4\u01f5\5C\"\2\u01f5\u00a6\3\2\2\2\u01f6")
        buf.write("\u01f8\t\4\2\2\u01f7\u01f6\3\2\2\2\u01f8\u01f9\3\2\2\2")
        buf.write("\u01f9\u01f7\3\2\2\2\u01f9\u01fa\3\2\2\2\u01fa\u00a8\3")
        buf.write("\2\2\2\u01fb\u01fd\t\4\2\2\u01fc\u01fb\3\2\2\2\u01fd\u01fe")
        buf.write("\3\2\2\2\u01fe\u01fc\3\2\2\2\u01fe\u01ff\3\2\2\2\u01ff")
        buf.write("\u020d\3\2\2\2\u0200\u0204\7\60\2\2\u0201\u0203\t\4\2")
        buf.write("\2\u0202\u0201\3\2\2\2\u0203\u0206\3\2\2\2\u0204\u0202")
        buf.write("\3\2\2\2\u0204\u0205\3\2\2\2\u0205\u0208\3\2\2\2\u0206")
        buf.write("\u0204\3\2\2\2\u0207\u0209\5\63\32\2\u0208\u0207\3\2\2")
        buf.write("\2\u0208\u0209\3\2\2\2\u0209\u020b\3\2\2\2\u020a\u0200")
        buf.write("\3\2\2\2\u020a\u020b\3\2\2\2\u020b\u020e\3\2\2\2\u020c")
        buf.write("\u020e\5\63\32\2\u020d\u020a\3\2\2\2\u020d\u020c\3\2\2")
        buf.write("\2\u020e\u021b\3\2\2\2\u020f\u0211\7\60\2\2\u0210\u0212")
        buf.write("\t\4\2\2\u0211\u0210\3\2\2\2\u0212\u0213\3\2\2\2\u0213")
        buf.write("\u0211\3\2\2\2\u0213\u0214\3\2\2\2\u0214\u0216\3\2\2\2")
        buf.write("\u0215\u0217\5\63\32\2\u0216\u0215\3\2\2\2\u0216\u0217")
        buf.write("\3\2\2\2\u0217\u021b\3\2\2\2\u0218\u0219\7\60\2\2\u0219")
        buf.write("\u021b\5\63\32\2\u021a\u01fc\3\2\2\2\u021a\u020f\3\2\2")
        buf.write("\2\u021a\u0218\3\2\2\2\u021b\u00aa\3\2\2\2\u021c\u021d")
        buf.write("\5\u00b1Y\2\u021d\u021e\7$\2\2\u021e\u021f\bV\3\2\u021f")
        buf.write("\u00ac\3\2\2\2\u0220\u0222\t\37\2\2\u0221\u0220\3\2\2")
        buf.write("\2\u0222\u0226\3\2\2\2\u0223\u0225\t \2\2\u0224\u0223")
        buf.write("\3\2\2\2\u0225\u0228\3\2\2\2\u0226\u0224\3\2\2\2\u0226")
        buf.write("\u0227\3\2\2\2\u0227\u00ae\3\2\2\2\u0228\u0226\3\2\2\2")
        buf.write("\u0229\u022b\t!\2\2\u022a\u0229\3\2\2\2\u022b\u022c\3")
        buf.write("\2\2\2\u022c\u022a\3\2\2\2\u022c\u022d\3\2\2\2\u022d\u022e")
        buf.write("\3\2\2\2\u022e\u022f\bX\2\2\u022f\u00b0\3\2\2\2\u0230")
        buf.write("\u0236\7$\2\2\u0231\u0232\7^\2\2\u0232\u0235\t\"\2\2\u0233")
        buf.write("\u0235\n#\2\2\u0234\u0231\3\2\2\2\u0234\u0233\3\2\2\2")
        buf.write("\u0235\u0238\3\2\2\2\u0236\u0234\3\2\2\2\u0236\u0237\3")
        buf.write("\2\2\2\u0237\u0239\3\2\2\2\u0238\u0236\3\2\2\2\u0239\u023a")
        buf.write("\bY\4\2\u023a\u00b2\3\2\2\2\u023b\u023c\5\u00b1Y\2\u023c")
        buf.write("\u023d\7^\2\2\u023d\u023e\n\"\2\2\u023e\u023f\bZ\5\2\u023f")
        buf.write("\u00b4\3\2\2\2\u0240\u0241\13\2\2\2\u0241\u0242\b[\6\2")
        buf.write("\u0242\u00b6\3\2\2\2\31\2\u00ec\u00f8\u0105\u010b\u0114")
        buf.write("\u0119\u0151\u01f9\u01fe\u0204\u0208\u020a\u020d\u0213")
        buf.write("\u0216\u021a\u0221\u0224\u0226\u022c\u0234\u0236\7\b\2")
        buf.write("\2\3V\2\3Y\3\3Z\4\3[\5")
        return buf.getvalue()


class MPLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    ADD = 1
    SUB = 2
    MUL = 3
    DIVISION = 4
    EQUAL = 5
    NOTEQUAL = 6
    LT = 7
    LE = 8
    GE = 9
    GT = 10
    LB = 11
    RB = 12
    LSB = 13
    RSB = 14
    LP = 15
    RP = 16
    SEMI = 17
    COLON = 18
    COMMA = 19
    DOUBLEDOT = 20
    ASSIGN = 21
    CMT1 = 22
    CMT2 = 23
    CMT3 = 24
    BOOLEANLIT = 25
    VAR = 26
    FUNCTION = 27
    PROCEDURE = 28
    BREAK = 29
    CONTINUE = 30
    FOR = 31
    TO = 32
    DOWNTO = 33
    DO = 34
    IF = 35
    THEN = 36
    ELSE = 37
    RETURN = 38
    WHILE = 39
    BEGIN = 40
    END = 41
    TRUE = 42
    FALSE = 43
    ARRAY = 44
    OF = 45
    INTEGER = 46
    BOOLEAN = 47
    REAL = 48
    STRING = 49
    NOT = 50
    AND = 51
    OR = 52
    DIV = 53
    MOD = 54
    WITH = 55
    INTLIT = 56
    REALLIT = 57
    STRINGLIT = 58
    ID = 59
    WS = 60
    UNCLOSESTRING = 61
    ILLEGALESCAPE = 62
    ERRORCHAR = 63

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'-'", "'*'", "'/'", "'='", "'<>'", "'<'", "'<='", "'>='", 
            "'>'", "'('", "')'", "'['", "']'", "'{'", "'}'", "';'", "':'", 
            "','", "'..'", "':='" ]

    symbolicNames = [ "<INVALID>",
            "ADD", "SUB", "MUL", "DIVISION", "EQUAL", "NOTEQUAL", "LT", 
            "LE", "GE", "GT", "LB", "RB", "LSB", "RSB", "LP", "RP", "SEMI", 
            "COLON", "COMMA", "DOUBLEDOT", "ASSIGN", "CMT1", "CMT2", "CMT3", 
            "BOOLEANLIT", "VAR", "FUNCTION", "PROCEDURE", "BREAK", "CONTINUE", 
            "FOR", "TO", "DOWNTO", "DO", "IF", "THEN", "ELSE", "RETURN", 
            "WHILE", "BEGIN", "END", "TRUE", "FALSE", "ARRAY", "OF", "INTEGER", 
            "BOOLEAN", "REAL", "STRING", "NOT", "AND", "OR", "DIV", "MOD", 
            "WITH", "INTLIT", "REALLIT", "STRINGLIT", "ID", "WS", "UNCLOSESTRING", 
            "ILLEGALESCAPE", "ERRORCHAR" ]

    ruleNames = [ "ADD", "SUB", "MUL", "DIVISION", "EQUAL", "NOTEQUAL", 
                  "LT", "LE", "GE", "GT", "LB", "RB", "LSB", "RSB", "LP", 
                  "RP", "SEMI", "COLON", "COMMA", "DOUBLEDOT", "ASSIGN", 
                  "CMT1", "CMT2", "CMT3", "EXPONENT", "A", "B", "C", "D", 
                  "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", 
                  "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", 
                  "BOOLEANLIT", "VAR", "FUNCTION", "PROCEDURE", "BREAK", 
                  "CONTINUE", "FOR", "TO", "DOWNTO", "DO", "IF", "THEN", 
                  "ELSE", "RETURN", "WHILE", "BEGIN", "END", "TRUE", "FALSE", 
                  "ARRAY", "OF", "INTEGER", "BOOLEAN", "REAL", "STRING", 
                  "NOT", "AND", "OR", "DIV", "MOD", "WITH", "INTLIT", "REALLIT", 
                  "STRINGLIT", "ID", "WS", "UNCLOSESTRING", "ILLEGALESCAPE", 
                  "ERRORCHAR" ]

    grammarFileName = "MP.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[84] = self.STRINGLIT_action 
            actions[87] = self.UNCLOSESTRING_action 
            actions[88] = self.ILLEGALESCAPE_action 
            actions[89] = self.ERRORCHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text[1:-1]
     

    def UNCLOSESTRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise UncloseString(self.text[1:])
     

    def ILLEGALESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            raise IllegalEscape(self.text[1:])
     

    def ERRORCHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise ErrorToken(self.text)
     


