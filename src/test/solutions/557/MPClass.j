.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static a I
.field static b I

.method public static foo()V
Label0:
.var 0 is a I from Label2 to Label3
.var 1 is b I from Label2 to Label3
Label2:
.var 2 is c F from Label4 to Label5
Label4:
	iconst_1
	istore_0
	iconst_3
	istore_1
	iconst_4
	i2f
	fstore_2
	iload_0
	i2f
	iload_1
	i2f
	fload_2
	fmul
	fadd
	invokestatic io/putFloat(F)V
Label5:
Label3:
	nop
Label1:
	return
.limit stack 6
.limit locals 3
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	invokestatic MPClass/foo()V
	nop
Label1:
	return
.limit stack 0
.limit locals 1
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
