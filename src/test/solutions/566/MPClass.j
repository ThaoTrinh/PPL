.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static c I
.field static b I

.method public static foo(II)V
.var 0 is a I from Label0 to Label1
.var 1 is b I from Label0 to Label1
.var 2 is d Z from Label0 to Label1
Label0:
	invokestatic MPClass/foo1()Z
	istore_2
	iload_2
	invokestatic io/putBool(Z)V
	iload_0
	iconst_2
	if_icmpne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifeq Label4
	iconst_1
	istore_0
Label8:
	iload_0
	bipush 7
	if_icmpgt Label9
	iconst_1
	goto Label10
Label9:
	iconst_0
Label10:
	ifeq Label7
	iload_0
	iconst_5
	if_icmpne Label11
	iconst_1
	goto Label12
Label11:
	iconst_0
Label12:
	ifeq Label13
	goto Label7
	goto Label14
Label13:
	goto Label6
Label14:
	goto Label6
Label6:
	iload_0
	iconst_1
	iadd
	istore_0
	goto Label8
Label7:
	goto Label5
Label4:
Label5:
	iload_0
	invokestatic io/putInt(I)V
	nop
Label1:
	return
.limit stack 12
.limit locals 3
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_2
	iconst_2
	invokestatic MPClass/foo(II)V
	nop
Label1:
	return
.limit stack 4
.limit locals 1
.end method

.method public static foo1()Z
Label0:
	iconst_1
	ireturn
	nop
Label1:
.limit stack 2
.limit locals 0
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
