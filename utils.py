from outline_vpn import OutlineVPN

client = OutlineVPN(api_url=(
    "https://87.247.142.222:63164/CtykuO9_lRq6hgdCNjeFow"
),
    cert_sha256=(
    "8D876891BEE756FC2CF72E0683EA99807A860974F6976951D3942DFE7226BC9D"
))


def get_new_key(name):
    new_key = client.create_key()
    client.rename_key(new_key.key_id, name)
    return new_key


def delete_all_keys():
    for key in client.get_keys():
        client.delete_key(key.key_id)


def get_all_keys():
    return [key.name for key in client.get_keys()]


def delete_key(name):
    for key in client.get_keys():
        if key.name == name:
            client.delete_key(key.key_id)
            return True



def all_keys_str():
    all_keys = ''
    for name in get_all_keys():
        all_keys += f'{name}, '
    return all_keys
