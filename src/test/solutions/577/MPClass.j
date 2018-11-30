.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static a I
.field static b F
.field static c F

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is d Z from Label0 to Label1
Label0:
.var 2 is e F from Label2 to Label3
Label2:
.var 3 is e I from Label4 to Label5
Label4:
	iconst_1
	istore_3
	iload_3
	invokestatic io/putInt(I)V
Label5:
Label3:
	nop
Label1:
	return
.limit stack 2
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
