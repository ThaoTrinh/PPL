.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static foo(FFZ)F
.var 0 is a F from Label0 to Label1
.var 1 is b F from Label0 to Label1
.var 2 is d Z from Label0 to Label1
Label0:
	bipush 6
	i2f
	freturn
	nop
Label1:
.limit stack 2
.limit locals 3
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a F from Label0 to Label1
Label0:
	iconst_1
	i2f
	iconst_2
	i2f
	iconst_1
	invokestatic MPClass/foo(FFZ)F
	fstore_1
	fload_1
	invokestatic io/putFloat(F)V
	nop
Label1:
	return
.limit stack 6
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
