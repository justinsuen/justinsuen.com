<?php
/**
 * The base configurations of the WordPress.
 *
 * This file has the following configurations: MySQL settings, Table Prefix,
 * Secret Keys, WordPress Language, and ABSPATH. You can find more information
 * by visiting {@link http://codex.wordpress.org/Editing_wp-config.php Editing
 * wp-config.php} Codex page. You can get the MySQL settings from your web host.
 *
 * This file is used by the wp-config.php creation script during the
 * installation. You don't have to use the web site, you can just copy this file
 * to "wp-config.php" and fill in the values.
 *
 * @package WordPress
 */

// ** MySQL settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define('DB_NAME', 'justinsuen_com');

/** MySQL database username */
define('DB_USER', 'justinsuencom');

/** MySQL database password */
define('DB_PASSWORD', 'u!-ygpQH');

/** MySQL hostname */
define('DB_HOST', 'mysql.justinsuen.com');

/** Database Charset to use in creating database tables. */
define('DB_CHARSET', 'utf8');

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
define('AUTH_KEY',         'hZ*ZN0OU#2T8@(Q:?_Uhvqi*837:z3vKEH!a~E83BJMT@z_|IXhQNfXc"%A`Z|JD');
define('SECURE_AUTH_KEY',  'nSTwo^_3hcxH9CjOe8ia7/QyJIASh)SlReUxecoaQ_JX!MrsWkaHPX157nNVH/U3');
define('LOGGED_IN_KEY',    'PeLS;$|1pXWDpxz":ix0aPl4$R3iuf:fi)aFqDN)%$$+P"%*bqR?8CZrXT4v3el`');
define('NONCE_KEY',        '8p|()YUHx3GIP*x/T0f7id/p^0)ua42!(ipCg+Pg*^!);29yi#4ceXokgJw:~4la');
define('AUTH_SALT',        '01Uytoj&kEhEo#cOy02se!n&Y1s&PpKyOJNR(mGHidTNYo3|iBOQ)|fPF5X)T_0)');
define('SECURE_AUTH_SALT', 'WBK2%J(!OOPVJxr`SYkmwuUADdj/;Iv_2n8(vc~A9!lf8RIhYslCCI1D6#uRwm@C');
define('LOGGED_IN_SALT',   's8^0yrS`bw#7)8N2Rf?;CEM?REvwbbW/4%;gQZCWi7P$_13fx)TUN2i($*LI:R:F');
define('NONCE_SALT',       'r2aDLjp%cxTTjiIa?:Ggzpr($:PD?48sSCaB`pv2Z(ivM!:v~5Q^dcA;/iCPLD?|');

/**#@-*/

/**
 * WordPress Database Table prefix.
 *
 * You can have multiple installations in one database if you give each a unique
 * prefix. Only numbers, letters, and underscores please!
 */
$table_prefix  = 'wp_w9p582_';

/**
 * Limits total Post Revisions saved per Post/Page.
 * Change or comment this line out if you would like to increase or remove the limit.
 */
define('WP_POST_REVISIONS',  10);

/**
 * WordPress Localized Language, defaults to English.
 *
 * Change this to localize WordPress. A corresponding MO file for the chosen
 * language must be installed to wp-content/languages. For example, install
 * de_DE.mo to wp-content/languages and set WPLANG to 'de_DE' to enable German
 * language support.
 */
define('WPLANG', '');

/**
 * For developers: WordPress debugging mode.
 *
 * Change this to true to enable the display of notices during development.
 * It is strongly recommended that plugin and theme developers use WP_DEBUG
 * in their development environments.
 */
define('WP_DEBUG', false);

/* That's all, stop editing! Happy blogging. */

/** Absolute path to the WordPress directory. */
if ( !defined('ABSPATH') )
	define('ABSPATH', dirname(__FILE__) . '/');

/** Sets up WordPress vars and included files. */
require_once(ABSPATH . 'wp-settings.php');

