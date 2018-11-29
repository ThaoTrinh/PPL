.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static a F

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	ldc 9.5
	putstatic MPClass/a F
.var 1 is a I from Label2 to Label3
.var 2 is b I from Label2 to Label3
Label2:
	sipush 859
	istore_2
	iload_2
	sipush 179
	isub
	istore_1
Label3:
	getstatic MPClass/a F
	invokestatic io/putFloat(F)V
Label1:
	return
.limit stack 4
.limit locals 3
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
