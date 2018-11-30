.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is x I from Label0 to Label1
Label0:
	iconst_1
	iconst_1
	ineg
	i2f
	bipush 10
	bipush 70
	bipush 10
	iadd
	i2f
	invokestatic MPClass/foo(IFIF)F
	invokestatic io/putFloat(F)V
	nop
Label1:
	return
.limit stack 10
.limit locals 2
.end method

.method public static foo(IFIF)F
.var 0 is x I from Label0 to Label1
.var 1 is y F from Label0 to Label1
.var 2 is z I from Label0 to Label1
.var 3 is t F from Label0 to Label1
Label0:
	iload_0
	i2f
	fload_1
	fadd
	iload_2
	i2f
	fadd
	fload_3
	fadd
	freturn
	nop
Label1:
.limit stack 2
.limit locals 4
.end method

.method public <init>()V
.var 0 is this LMPClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
	nop
Label1:
	return
.limit stack 1
.limit locals 1
.end method
