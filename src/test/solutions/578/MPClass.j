.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static a I
.field static b F
.field static c F

.method public static foo()V
Label0:
	iconst_1
	invokestatic io/putInt(I)V
	nop
Label1:
	return
.limit stack 2
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is d Z from Label0 to Label1
Label0:
	invokestatic MPClass/foo()V
	nop
Label1:
	return
.limit stack 0
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
