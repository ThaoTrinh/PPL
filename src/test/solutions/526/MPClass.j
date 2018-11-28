.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a I from Label0 to Label1
.var 2 is b I from Label0 to Label1
.var 3 is c I from Label0 to Label1
Label0:
	bipush 10
	istore_1
	iconst_0
	istore_2
	iconst_0
	istore_3
Label2:
	iload_2
	iload_1
	if_icmpge Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifeq Label3
	iload_2
	iconst_1
	iadd
	istore_2
	iload_2
	bipush 7
	if_icmpne Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifeq Label8
	goto Label2
	goto Label9
Label8:
Label9:
	iload_3
	iconst_1
	iadd
	istore_3
	goto Label2
Label3:
	iload_3
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 12
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
