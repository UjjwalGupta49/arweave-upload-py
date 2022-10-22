from multiprocessing.heap import Arena
from turtle import up
import arweave
import utils 

wallet = utils.wallet

balance =  wallet.balance
print(balance)

lastTransaction = wallet.get_last_transaction_id()
print(lastTransaction)


# Upload the file to arweave and give explorer link, link to metadata

def dataUpload(wallet):
    transaction = arweave.Transaction(wallet=wallet, data= "HARD WORK IS WORTHLESS FOR THOSE THAT DONT BELIEVE IN THEMSELVES. NARUTO UZUMAKI")
    transaction.sign()
    transaction.send()

    uploadTransaction = wallet.get_last_transaction_id()
    getTx = arweave.Transaction(wallet=wallet, id= uploadTransaction)
    uploadTransactiondata = getTx.get_transaction()
    print(uploadTransactiondata)


dataUpload(wallet=wallet)