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
.var 2 is c I from Label4 to Label5
Label4:
	iconst_0
	istore_0
	iconst_0
	istore_1
	iconst_3
	istore_2
Label6:
	iload_0
	iload_2
	if_icmple Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifeq Label7
	iload_0
	iconst_1
	iadd
	istore_0
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label6
Label7:
	iload_1
	invokestatic io/putInt(I)V
Label5:
Label3:
Label1:
	return
.limit stack 9
.limit locals 3
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	invokestatic MPClass/foo()V
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
Label1:
	return
.limit stack 1
.limit locals 1
.end method
