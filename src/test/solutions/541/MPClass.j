.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_1
	iconst_2
	if_icmple Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifeq Label6
	iconst_3
	iconst_4
	if_icmpge Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifeq Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	iconst_1
	iconst_2
	if_icmpge Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	iand
	invokestatic io/putBool(Z)V
Label1:
	return
.limit stack 15
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
