import time
from behave import *
from Features.steps.Loginpages import Loginpage


@given(u'I am on homepage')
def step_impl(context):
    time.sleep(5)




@when(u'I search a product')
def step_impl(context):
    context.page_login = Loginpage(context.driver)
    context.page_login.login_my_account()
    context.page_login.search_product()



@then(u'I should see the product page')
def step_impl(context):
    context.page_login.verify_product()


