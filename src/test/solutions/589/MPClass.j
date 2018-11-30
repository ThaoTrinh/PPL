.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a I from Label0 to Label1
.var 2 is b I from Label0 to Label1
Label0:
.var 3 is a I from Label2 to Label3
.var 4 is b F from Label2 to Label3
Label2:
	bipush 6
	istore_3
	bipush 10
	i2f
	fstore 4
	fload 4
	iload_3
	i2f
	fcmpl
	ifle Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifeq Label6
	return
	goto Label7
Label6:
Label7:
Label3:
	bipush 100
	invokestatic io/putInt(I)V
	nop
Label1:
	return
.limit stack 6
.limit locals 5
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
