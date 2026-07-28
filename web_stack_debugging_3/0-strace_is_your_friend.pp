# Fixes a typo in wp-settings.php where class-wp-locale.phpp has an extra 'p'

exec { 'fix-wordpress':
  command => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
  path    => ['/bin', '/usr/bin'],
  onlyif  => 'grep -q "phpp" /var/www/html/wp-settings.php',
}
