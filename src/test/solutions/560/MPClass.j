.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static c I
.field static b I

.method public static foo(II)V
.var 0 is a I from Label0 to Label1
.var 1 is b I from Label0 to Label1
Label0:
	iload_0
	putstatic MPClass/c I
Label2:
	getstatic MPClass/c I
	iload_1
	if_icmpgt Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifeq Label3
	getstatic MPClass/c I
	iconst_1
	iadd
	putstatic MPClass/c I
	getstatic MPClass/c I
	invokestatic io/putInt(I)V
	goto Label2
Label3:
Label1:
	return
.limit stack 5
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_1
	iconst_2
	invokestatic MPClass/foo(II)V
Label1:
	return
.limit stack 4
.limit locals 1
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
