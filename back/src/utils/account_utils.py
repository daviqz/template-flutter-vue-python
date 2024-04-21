def validate_fields_register_account(username, email, password, password_confirm):
    field_errors = []

    if len(username) <= 2:
        error = {
            "message": "Nome de usuário precisa conter mais de 2 caracteres",
            "field": "username",
            "type": "ERROR",
        }
        field_errors.append(error)
    if len(email) <= 4:
        error = {
            "message": "Email precisa conter mais de 4 caracteres",
            "field": "email",
            "type": "ERROR",
        }
        field_errors.append(error)
    if len(password) <= 5:
        error = {
            "message": "A senha precisa conter mais de 5 caracteres",
            "field": "password",
            "type": "ERROR",
        }
        field_errors.append(error)
    if password != password_confirm:
        error = {
            "message": "Confirmação de senha diferente",
            "field": "password_confirm",
            "type": "ERROR",
        }
        field_errors.append(error)

    return {"is_valid": len(field_errors) == 0, "field_errors": field_errors}


def validate_fields_login(email, password):
    field_errors = []

    if len(email) <= 4:
        error = {
            "message": "Email precisa conter mais de 4 caracteres",
            "field": "username",
            "type": "ERROR",
        }
        field_errors.append(error)
    if len(password) <= 5:
        error = {
            "message": "A senha precisa conter mais de 5 caracteres",
            "field": "email",
            "type": "ERROR",
        }
        field_errors.append(error)

    return {"is_valid": len(field_errors) == 0, "field_errors": field_errors}
