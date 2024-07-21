def hitung_luas(panjang, lebar):
  """
  Fungsi untuk menghitung luas persegi panjang.

  Args:
    panjang: Nilai panjang persegi panjang (float).
    lebar: Nilai lebar persegi panjang (float).

  Returns:
    Nilai luas persegi panjang (float).
  """
  if panjang <= 0 or lebar <= 0:
    raise ValueError("Nilai panjang dan lebar harus positif!")
  return panjang * lebar


def hitung_keliling(panjang, lebar):
  """
  Fungsi untuk menghitung keliling persegi panjang.

  Args:
    panjang: Nilai panjang persegi panjang (float).
    lebar: Nilai lebar persegi panjang (float).

  Returns:
    Nilai keliling persegi panjang (float).
  """
  if panjang <= 0 or lebar <= 0:
    raise ValueError("Nilai panjang dan lebar harus positif!")
  return 2 * (panjang + lebar)


def hitung_diagonal(panjang, lebar):
  """
  Fungsi untuk menghitung diagonal persegi panjang.

  Args:
    panjang: Nilai panjang persegi panjang (float).
    lebar: Nilai lebar persegi panjang (float).

  Returns:
    Nilai diagonal persegi panjang (float).
  """
  if panjang <= 0 or lebar <= 0:
    raise ValueError("Nilai panjang dan lebar harus positif!")
  return (panjang * 2 + lebar * 2) ** 0.5


def main():
  """
  Fungsi utama untuk menjalankan program.
  """
  print("* Program Menghitung Luas, Keliling, dan Diagonal Persegi Panjang *")

  try:
    panjang = float(input("Masukan panjang persegi panjang: "))
    lebar = float(input("Masukan lebar persegi panjang: "))

    luas = hitung_luas(panjang, lebar)
    keliling = hitung_keliling(panjang, lebar)
    diagonal = hitung_diagonal(panjang, lebar)

    print(f"Luas persegi panjang: {luas}")
    print(f"Keliling persegi panjang: {keliling}")
    print(f"Diagonal persegi panjang: {diagonal}")
  except ValueError as e:
    print(f"Error: {e}")


if __name__ == "__main__":
  main()

