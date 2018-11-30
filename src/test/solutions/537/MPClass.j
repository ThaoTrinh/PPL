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
Label4:
	iload_1
	bipush 7
	if_icmpgt Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifeq Label3
	iconst_5
	istore_2
Label9:
	iload_2
	iconst_3
	if_icmplt Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifeq Label8
	goto Label7
Label7:
	iload_2
	iconst_1
	isub
	istore_2
	goto Label9
Label8:
	goto Label2
Label2:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label4
Label3:
	iload_3
	invokestatic io/putInt(I)V
	nop
Label1:
	return
.limit stack 11
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
