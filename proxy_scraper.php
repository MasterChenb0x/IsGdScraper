#!/usr/bin/env php
<?php
// Gr3y M4tt3r <gr3y@boycottbabies.org>
// 2010
// scrapes 9 pages of proxies from samair.ru and saves to fresh_proxies.txt

if ($argc == 0)
{
    show_source(__FILE__);
    die();
}

$verbosity = isset($argv[1]) ? $argv[1] : '';

function contains($haystack, $needle)
{
    if ( strpos($haystack, $needle) !== false )
        return true;
    else
        return false;
}

function get_proxies($num)
{
    global $verbosity;
    $port_digits = array('');
    $port_letters = array('+');

    $list = file_get_contents("http://www.samair.ru/proxy/time-0$num.htm");

    //get port number replacements..
    $pattern = '/(\w)=(\d);(\w)=(\d);(\w)=(\d);(\w)=(\d);(\w)=(\d);(\w)=(\d);(\w)=(\d);(\w)=(\d);(\w)=(\d);(\w)=(\d);<\/script><\/head>/s';
    preg_match($pattern, $list, $matches);

    for ($i=1; $i<=20; $i += 2) {
        $port_letters[] = $matches[$i];
        $port_digits[] =  $matches[$i + 1];
    }

    //get ip addresses and masked ports...
    $pattern = '/(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).+?\(":"(.+?)\)/x';
    preg_match_all($pattern, $list, $matches);
    foreach ($matches[1] as $k => $ip) {
        $matches[1][$k] = $ip.':'.str_replace($port_letters, $port_digits, $matches[2][$k]);
        if ( contains($verbosity,'vvv') )
            echo '* '.$matches[1][$k]."\n";
    }
    if ( contains($verbosity,'vv') )
        echo ''.count($matches[1])." proxies scraped...\n";
    return $matches[1];
}

if ( contains($verbosity,'v') ) //if user wants verbose output
    echo "Retriving list of proxies from samair.ru...\n";

$proxies = array();
for ($num = 1; $num < 10; $num++) //get 9 pages of proxies.
{
    $per = get_proxies($num);
    foreach ($per as $p)
        $proxies[] = $p."\n";
}
if ( contains($verbosity,'v') ) //if user wants verbose output
    echo 'Writing list of '.count($proxies)." proxies to file...\n";

file_put_contents('fresh_proxies.txt',$proxies);
?>

