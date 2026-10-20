def validar_email(email: str) -> bool:
    """Valida formato básico: usuário@dominio.extensao."""
    if not isinstance(email, str):
        return False

    email = email.strip()

    # Deve conter exatamente um @
    if email.count("@") != 1:
        return False

    usuario, dominio = email.split("@")

    # Usuário e domínio não podem estar vazios
    if not usuario or not dominio:
        return False

    # Domínio deve ter pelo menos um ponto e não pode começar/terminar com ponto
    if "." not in dominio or dominio.startswith(".") or dominio.endswith("."):
        return False

    # A extensão do domínio (TLD) deve ter pelo menos 2 caracteres
    extensao = dominio.split(".")[-1]
    if len(extensao) < 2:
        return False

    return True