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
	iconst_1
	istore_1
	iload_1
	ifeq Label2
	iconst_5
	ineg
	i2f
	iconst_2
	iconst_5
	imul
	i2f
	fdiv
	iconst_3
	i2f
	fadd
	invokestatic io/putFloat(F)V
	goto Label3
Label2:
Label3:
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
