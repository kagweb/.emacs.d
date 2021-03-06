kind=added
names=wont_respond_to
visibility=public 

--- wont_respond_to(method_name) -> true

自身が与えられたメソッドを持たない場合、検査にパスしたことになります。

@param method_name メソッド名を指定します。

@raise MiniTest::Assertion 自身が与えられたメソッドを持つ場合に発生します。

@see [[m:MiniTest::Assertions#refute_respond_to]]

