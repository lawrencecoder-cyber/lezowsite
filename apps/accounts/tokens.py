from django.contrib.auth.tokens import PasswordResetTokenGenerator


class AccountTokenGenerator(PasswordResetTokenGenerator):
    pass


account_token = AccountTokenGenerator()



class EmailVerificationTokenGenerator(PasswordResetTokenGenerator):
    pass


email_token_generator = EmailVerificationTokenGenerator()
