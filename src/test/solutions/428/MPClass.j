.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a I from Label0 to Label1
Label0:
	bipush 10
	istore_1
Label4:
	iload_1
	iconst_0
	if_icmplt Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifeq Label3
	iload_1
	iconst_1
	isub
	istore_1
	goto Label2
Label2:
	iload_1
	iconst_1
	isub
	istore_1
	goto Label4
Label3:
	iload_1
	invokestatic io/putInt(I)V
	nop
Label1:
	return
.limit stack 7
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
