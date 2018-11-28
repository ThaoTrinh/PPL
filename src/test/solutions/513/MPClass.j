.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static x I
.field static y I
.field static a F
.field static b F
.field static c F

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is x F from Label0 to Label1
.var 2 is y F from Label0 to Label1
Label0:
	invokestatic MPClass/foo()V
Label1:
	return
.limit stack 0
.limit locals 3
.end method

.method public static foo()V
.var 0 is x F from Label0 to Label1
.var 1 is y F from Label0 to Label1
Label0:
Label1:
	return
.limit stack 0
.limit locals 2
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
