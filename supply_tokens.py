from brownie import *


def main():
    testAccounts = [
        "0x9fde0c31B3b21E8031C08A5c43f851c9C6544E35",
        "0x5fe0676e41741A3a2d84C41DC46cC991812FE110",
        "0x5307DB0c8Fb2Dc616B94f3b2f9fe7a99920e5e52"
    ]

    # crvToken = Contract.from_explorer("0xD533a949740bb3306d119CC777fa900bA034cd52")
    # yfiToken = Contract.from_explorer("0x0bc529c00C6401aEF6D220BE8C6Ea1667F6Ad93e")
    usdcToken = Contract.from_explorer("0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48")

    # crvWhale = accounts.at("0x4ce799e6ed8d64536b67dd428565d52a531b3640", force=True)
    # yfiWhale = accounts.at("0xfeb4acf3df3cdea7399794d0869ef76a6efaff52", force=True)
    usdcWhale = accounts.at("0x397ff1542f962076d0bfe58ea045ffa2d347aca0", force=True)

    for account in testAccounts:
        # crvToken.transfer(account, "100", {'from': crvWhale})
        # yfiToken.transfer(account, "20", {'from': yfiWhale})
        usdcToken.transfer(account, "1000000000", {'from': usdcWhale})
