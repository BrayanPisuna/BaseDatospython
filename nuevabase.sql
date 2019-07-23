-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 23-07-2019 a las 03:10:53
-- Versión del servidor: 10.3.16-MariaDB
-- Versión de PHP: 7.3.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `usuarios`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `nuevabase`
--

CREATE TABLE `nuevabase` (
  `Id` varchar(25) NOT NULL,
  `nombre` varchar(25) NOT NULL,
  `apellido` varchar(25) NOT NULL,
  `fisica` varchar(2) NOT NULL,
  `matematica` varchar(2) NOT NULL,
  `sociales` varchar(2) NOT NULL,
  `lenguaje` varchar(2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `nuevabase`
--

INSERT INTO `nuevabase` (`Id`, `nombre`, `apellido`, `fisica`, `matematica`, `sociales`, `lenguaje`) VALUES
('', '', '', '', '', '', ''),
('1724358526', 'joel', 'pi', '10', '9', '8', '4'),
('125848', 'valen', 'pi', '10', '9', '8', '7'),
('172435', 'DAVID', 'PP', '10', '20', '30', '40'),
('1724358518', 'brayan david', 'pisuña paillacho', '10', '10', '10', '10');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
