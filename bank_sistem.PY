class BankAccount:

    def __init__(self, nama, saldo_awal):
        self.nama = nama
        self.saldo = saldo_awal

    def deposit(self, jumlah):
        if jumlah <= 0:
            print("Jumlah tidak valid")
        else:
            self.saldo += jumlah
            print("Deposit berhasil")

    def withdraw(self, jumlah):
        if jumlah > self.saldo:
            print("Saldo tidak cukup")
        else:
            self.saldo -= jumlah
            print("Withdraw berhasil")

    def tampilkan_info(self):
        print("Nama :", self.nama)
        print("Saldo :", self.saldo)


accounts = []

akun1 = BankAccount("Wan", 100000)
accounts.append(akun1)

akun1.deposit(50000)
akun1.withdraw(30000)

for acc in accounts:
    acc.tampilkan_info()