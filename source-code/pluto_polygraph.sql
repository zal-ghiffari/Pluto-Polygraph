-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 01 Sep 2022 pada 03.37
-- Versi server: 10.4.18-MariaDB
-- Versi PHP: 7.3.27

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pluto_polygraph`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `cases`
--

CREATE TABLE `cases` (
  `id` int(11) NOT NULL,
  `id_hex` varchar(255) NOT NULL,
  `id_hex_user` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `age` int(4) NOT NULL,
  `gender` varchar(255) NOT NULL,
  `cases` varchar(255) NOT NULL,
  `datetime` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `cases`
--

INSERT INTO `cases` (`id`, `id_hex`, `id_hex_user`, `name`, `age`, `gender`, `cases`, `datetime`) VALUES
(1, '41686d616420556c756c20416d726923323723323032322d30382d31372031343a30343a3538', '3123737570657275736572', 'Ahmad Ulul Amri', 27, 'Male', 'Pencurian Sepeda Motor', '2022-08-17 14:04:58');

-- --------------------------------------------------------

--
-- Struktur dari tabel `history`
--

CREATE TABLE `history` (
  `id` int(11) NOT NULL,
  `id_hex_user` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `cases` varchar(255) NOT NULL,
  `question` varchar(1000) NOT NULL,
  `result_truth` int(100) NOT NULL,
  `result_lie` int(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `history`
--

INSERT INTO `history` (`id`, `id_hex_user`, `name`, `cases`, `question`, `result_truth`, `result_lie`) VALUES
(1, '322370656e796964696b31', 'Mahmud Ali', 'Korupsi', 'Apakah benar anda menggelapkan uang yayasan?', 78, 22),
(2, '332370656e796964696b32', 'Almiska Bernadeta', 'Pencurian', 'Apakah anda membawa senjata tajam saat kejadian?', 69, 31),
(3, '332370656e796964696b32', 'Arki Lamasta', 'Pemerasan', 'Apakah benar anda memiliki rekening ada nama X?', 3, 97),
(7, '342370656e796964696b33', 'Adnil Maali', 'Penganiayaan', 'Apakah saudara sengaja memukul santri anda sendiri?', 51, 49),
(8, '322370656e796964696b31', 'Adnil Maali Test', 'Test', 'Test', 51, 49);

-- --------------------------------------------------------

--
-- Struktur dari tabel `interview`
--

CREATE TABLE `interview` (
  `id` int(11) NOT NULL,
  `id_hex_cases` varchar(255) NOT NULL,
  `question` varchar(255) NOT NULL,
  `truth` int(100) NOT NULL,
  `lie` int(100) NOT NULL,
  `datetime` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `interview`
--

INSERT INTO `interview` (`id`, `id_hex_cases`, `question`, `truth`, `lie`, `datetime`) VALUES
(1, '41686d616420556c756c20416d726923323723323032322d30382d31372031343a30343a3538', 'Apakah saudara sengaja memukul santri anda sendiri?', 52, 48, '2022-08-31 11:34:49'),
(2, '41686d616420556c756c20416d726923323723323032322d30382d31372031343a30343a3538', 'Apakah anda berasal dari semarang?', 54, 46, '2022-08-31 11:44:36');

-- --------------------------------------------------------

--
-- Struktur dari tabel `testing`
--

CREATE TABLE `testing` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `result_truth` int(100) NOT NULL,
  `result_lie` int(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `testing`
--

INSERT INTO `testing` (`id`, `name`, `result_truth`, `result_lie`) VALUES
(1, 'M Novrizal Ghiffari', 100, 100);

-- --------------------------------------------------------

--
-- Struktur dari tabel `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `id_hex` varchar(255) NOT NULL,
  `fullname` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `level` int(2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `users`
--

INSERT INTO `users` (`id`, `id_hex`, `fullname`, `email`, `username`, `password`, `level`) VALUES
(1, '3123737570657275736572', 'Super User', 'superuser@puslab.com', 'superuser', '$2a$12$Tb0C1PkbNdLx0dBeBA3ib.nzyiDWtMMtUcM5WixoMrNrAt55Mb.JK', 2),
(2, '322370656e796964696b31', 'Penyidik Pertama', 'penyidik1@puslab.com', 'penyidik1', '$2b$12$ao/l09Cjigs.f.QYb2cdY.zIAIs9k3lxk8kwbNqFOnEcxYwVWJcQy', 1),
(3, '332370656e796964696b32', 'Penyidik Kedua', 'penyidik2@puslab.com', 'penyidik2', '$2b$12$bDxkVduw3UMTXttVPPuFuODf2YM6YuLooWAGCbdraiKVJuXiulMoC', 1),
(4, '342370656e796964696b33', 'Penyidik Ketiga', 'penyidik3@puslab.com', 'penyidik3', '$2b$12$nDLcnhTeQqR1DFnMQanmn.wIpQUva9gcyKx9DrZgkLvdT1POWKj1O', 1);

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `cases`
--
ALTER TABLE `cases`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `history`
--
ALTER TABLE `history`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_hex_user` (`id_hex_user`);

--
-- Indeks untuk tabel `interview`
--
ALTER TABLE `interview`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `testing`
--
ALTER TABLE `testing`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_hex` (`id_hex`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `cases`
--
ALTER TABLE `cases`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT untuk tabel `history`
--
ALTER TABLE `history`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT untuk tabel `interview`
--
ALTER TABLE `interview`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT untuk tabel `testing`
--
ALTER TABLE `testing`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT untuk tabel `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
