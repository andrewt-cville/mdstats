<?php
/**
 * The base configuration for WordPress
 *
 * The wp-config.php creation script uses this file during the
 * installation. You don't have to use the web site, you can
 * copy this file to "wp-config.php" and fill in the values.
 *
 * This file contains the following configurations:
 *
 * * MySQL settings
 * * Secret keys
 * * Database table prefix
 * * ABSPATH
 *
 * @link https://codex.wordpress.org/Editing_wp-config.php
 *
 * @package WordPress
 */

// ** MySQL settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define('DB_NAME', 'wordpress');

/** MySQL database username */
define('DB_USER', 'root');

/** MySQL database password */
define('DB_PASSWORD', 'root');

/** MySQL hostname */
define('DB_HOST', 'localhost');

/** Database Charset to use in creating database tables. */
define('DB_CHARSET', 'utf8mb4');

/** The Database Collate type. Don't change this if in doubt. */
define('DB_COLLATE', '');

/**#@+
 * Authentication Unique Keys and Salts.
 *
 * Change these to different unique phrases!
 * You can generate these using the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}
 * You can change these at any point in time to invalidate all existing cookies. This will force all users to have to log in again.
 *
 * @since 2.6.0
 */
define('AUTH_KEY',         'DT$|?,c:=TT9V0Jr7JSg1E+|Mn!rKSVLE+LXsw]!yh}ae6~ [][O uJ9Xw./]vE`');
define('SECURE_AUTH_KEY',  'Q:U|j.a}CkR6ss&#E@J2hKEtWZOp23ZCG[cc&IQ*a6atdj6B95I<Vt%yn9aqJ^dB');
define('LOGGED_IN_KEY',    'b&6e^&-! 0%NPF<l5j/,_zPw*:k9w>dA X-UF$MIgP8&M-5a-SP;GtI%4(ZS+3G*');
define('NONCE_KEY',        'X^eMZ([-_hI}MoYj$J]MxFtC<O|hesI_i8M{K;(f$5jxUJg]C!kA]]#EYc%.<`~M');
define('AUTH_SALT',        '&;1j),28hE? +H)9P:^%t[TvJ<OfW>vJkmFi9jK5vzINUiW?/wY$a)glm+oXbI4I');
define('SECURE_AUTH_SALT', '~Y`jJ2]=n2%CH*ZW>>p/ |Lg{~KJMIEzOCu  &e!Rt}j1<Z}[/Jn+X#?HfCdjM.s');
define('LOGGED_IN_SALT',   'TxR$8N05k:qx4Q?`K{dI}07I}0Jfw|?]6s+|k?j!W+()#{O (YM:)j@ VM|`dU^s');
define('NONCE_SALT',       '$/EEi:/9QfdBIR14FY^KyUYPfrKOYw-7[U>YD(Gm:ZOFn%hUJ)ykAGrQwY}R*LNW');

/**#@-*/

/**
 * WordPress Database Table prefix.
 *
 * You can have multiple installations in one database if you give each
 * a unique prefix. Only numbers, letters, and underscores please!
 */
$table_prefix  = 'wp_';

/**
 * For developers: WordPress debugging mode.
 *
 * Change this to true to enable the display of notices during development.
 * It is strongly recommended that plugin and theme developers use WP_DEBUG
 * in their development environments.
 *
 * For information on other constants that can be used for debugging,
 * visit the Codex.
 *
 * @link https://codex.wordpress.org/Debugging_in_WordPress
 */
define('WP_DEBUG', false);

/* That's all, stop editing! Happy blogging. */

/** Absolute path to the WordPress directory. */
if ( !defined('ABSPATH') )
	define('ABSPATH', dirname(__FILE__) . '/');

/** Sets up WordPress vars and included files. */
require_once(ABSPATH . 'wp-settings.php');
