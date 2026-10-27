<?php
/**
 * The base configuration for WordPress
 *
 * The wp-config.php creation script uses this file during the installation.
 * You don't have to use the website, you can copy this file to "wp-config.php"
 * and fill in the values.
 *
 * This file contains the following configurations:
 *
 * * Database settings
 * * Secret keys
 * * Database table prefix
 * * ABSPATH
 *
 * @link https://developer.wordpress.org/advanced-administration/wordpress/wp-config/
 *
 * @package WordPress
 */

// ** Database settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define( 'DB_NAME', 'bilety' );

/** Database username */
define( 'DB_USER', 'root' );

/** Database password */
define( 'DB_PASSWORD', '' );

/** Database hostname */
define( 'DB_HOST', 'localhost' );

/** Database charset to use in creating database tables. */
define( 'DB_CHARSET', 'utf8mb4' );

/** The database collate type. Don't change this if in doubt. */
define( 'DB_COLLATE', '' );

/**#@+
 * Authentication unique keys and salts.
 *
 * Change these to different unique phrases! You can generate these using
 * the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}.
 *
 * You can change these at any point in time to invalidate all existing cookies.
 * This will force all users to have to log in again.
 *
 * @since 2.6.0
 */
define( 'AUTH_KEY',         '{?;z|,zMXa-rW^e$--#VP{/o#l15$ [*QL`y7B[ja:J_&1YV&e}^{?ZvtH2Xqv2>' );
define( 'SECURE_AUTH_KEY',  'u`K0:.K/Xp5q@uwj(-*fN[`(Nhf2Q<F`%3rdX$=Ad(XV,sE)78T6nw6_<!8<}4;0' );
define( 'LOGGED_IN_KEY',    'b]%t#%puvoCmcC(@A$K^RVVbL|k~Up,qKu)gLOJ^DV:peAvS2wkcV: oc/c.l0Ul' );
define( 'NONCE_KEY',        'Xs<Ze/AT[V[cE+]|wR}[*p/Dm=j#_J-;^DqL(w`Ix.]wzGU?$>#[=6~S}cXB=HBb' );
define( 'AUTH_SALT',        '=O=b(#/)Pies8?(ZtzHOFnQ[G)p2R:LnvdvKTA||CZ|H7_]*HJxe__2.olu*NY]j' );
define( 'SECURE_AUTH_SALT', 'Xi]K</@enk/!3_nt (k<!{[?|T]2z(Kal=!K?g[o*zeFL2bCw</4uY*[aSMAth/z' );
define( 'LOGGED_IN_SALT',   'iy%3;$h6_0>.sOhkJsIr_#V<Am,!mgqZ#<1pT/V,qn$/LQOqBcd0*^H1OL`qzqV7' );
define( 'NONCE_SALT',       'HAr]Zc75BwWO,WkDvj-L1m GD!D,Y#8R8N*9QGh(p Dha@(eAgP}XhZQ$]6yy#JW' );

/**#@-*/

/**
 * WordPress database table prefix.
 *
 * You can have multiple installations in one database if you give each
 * a unique prefix. Only numbers, letters, and underscores please!
 *
 * At the installation time, database tables are created with the specified prefix.
 * Changing this value after WordPress is installed will make your site think
 * it has not been installed.
 *
 * @link https://developer.wordpress.org/advanced-administration/wordpress/wp-config/#table-prefix
 */
$table_prefix = 'wp_';

/**
 * For developers: WordPress debugging mode.
 *
 * Change this to true to enable the display of notices during development.
 * It is strongly recommended that plugin and theme developers use WP_DEBUG
 * in their development environments.
 *
 * For information on other constants that can be used for debugging,
 * visit the documentation.
 *
 * @link https://developer.wordpress.org/advanced-administration/debug/debug-wordpress/
 */
define( 'WP_DEBUG', false );

/* Add any custom values between this line and the "stop editing" line. */



/* That's all, stop editing! Happy publishing. */

/** Absolute path to the WordPress directory. */
if ( ! defined( 'ABSPATH' ) ) {
	define( 'ABSPATH', __DIR__ . '/' );
}

/** Sets up WordPress vars and included files. */
require_once ABSPATH . 'wp-settings.php';
