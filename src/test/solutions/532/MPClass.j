.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_1
	iconst_2
	if_icmpge Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifne Label6
	iconst_3
	iconst_4
	if_icmple Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifne Label6
	iconst_0
	goto Label7
Label6:
	iconst_1
Label7:
	invokestatic io/putBool(Z)V
Label1:
	return
.limit stack 10
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
