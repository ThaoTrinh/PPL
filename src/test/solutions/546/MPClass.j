.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static foo(IF)F
.var 0 is a I from Label0 to Label1
.var 1 is b F from Label0 to Label1
Label0:
	iload_0
	i2f
	fload_1
	fadd
	freturn
Label1:
.limit stack 2
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is c F from Label0 to Label1
Label0:
	iconst_1
	iconst_2
	i2f
	invokestatic MPClass/foo(IF)F
	fstore_1
	fload_1
	invokestatic io/putFloat(F)V
Label1:
	return
.limit stack 4
.limit locals 2
.end method

.method public <init>()V
.var 0 is this LMPClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method
