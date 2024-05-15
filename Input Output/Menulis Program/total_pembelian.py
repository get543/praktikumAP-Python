total_pembelian = int(input("Masukkan total pembelian: "));

total_ppn = total_pembelian * 0.1;
total_sc = total_pembelian * 0.05;
total_pembayaran = total_pembelian + total_ppn + total_sc;

print(f"Total Pembelian: Rp {total_pembelian:,.2f}");
print(f"PPN (10%): Rp {total_ppn:,.2f}");
print(f"Service Charge (5%): Rp {total_sc:,.2f}");
print(f"Total yang harus dibayarkan: Rp {total_pembayaran:,.2f}");