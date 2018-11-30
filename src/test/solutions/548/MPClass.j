.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a F from Label0 to Label1
.var 2 is b F from Label0 to Label1
Label0:
	bipush 100
	i2f
	fstore_1
	iconst_0
	i2f
	fstore_2
Label2:
	fload_1
	fload_2
	fsub
	iconst_0
	i2f
	fcmpl
	ifeq Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifeq Label3
	fload_2
	iconst_1
	i2f
	fadd
	fstore_2
	goto Label2
Label3:
	fload_2
	ldc 100.0
	fcmpl
	ifne Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifeq Label8
	ldc "ok"
	invokestatic io/putString(Ljava/lang/String;)V
	return
	goto Label9
Label8:
Label9:
	nop
Label1:
	return
.limit stack 9
.limit locals 3
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
