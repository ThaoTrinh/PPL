.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a F from Label0 to Label1
Label0:
	ldc 1.123
	fstore_1
	fload_1
	fneg
	fstore_1
	fload_1
	invokestatic io/putFloat(F)V
	nop
Label1:
	return
.limit stack 1
.limit locals 2
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
