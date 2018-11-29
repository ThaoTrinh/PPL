.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a I from Label0 to Label1
.var 2 is b I from Label0 to Label1
.var 3 is c I from Label0 to Label1
Label0:
	iconst_0
	istore_3
	iconst_3
	istore_1
Label2:
	iload_1
	bipush 7
	if_icmpgt Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifeq Label3
	iconst_5
	istore_2
Label6:
	iload_2
	iconst_3
	if_icmplt Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifeq Label7
	iload_3
	iconst_1
	iadd
	istore_3
	iload_2
	iconst_1
	isub
	istore_2
	goto Label6
Label7:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label2
Label3:
	iload_3
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 14
.limit locals 4
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
