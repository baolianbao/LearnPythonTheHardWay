# class Parent(object):
#
#     def implicit(self):
#         print "PARENT implicit()"
#
# class Child(Parent):
#     pass
#
# dad = Parent()
# son = Child()
#
# dad.implicit()
# son.implicit()


class Parent(object):
  def override(self):
    print "PARENT override()"

class Child(Parent):
  def override(self):
    print "CHILD override()"

dad = Parent()
son = Child()

dad.override()
son.override()
