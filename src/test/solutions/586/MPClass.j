.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a I from Label2 to Label3
.var 2 is b F from Label2 to Label3
Label2:
	bipush 6
	istore_1
	bipush 10
	i2f
	fstore_2
	iload_1
	i2f
	fload_2
	fadd
	invokestatic io/putFloat(F)V
Label3:
	nop
Label1:
	return
.limit stack 4
.limit locals 3
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
