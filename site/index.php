<html>
  <body>
    <h1>Ads</h1>
    <ul>
       <?php
      $ad_sn = 1;
        $json = file_get_contents('http://apts');
        $ads_items = json_decode($json);
        foreach ($ads_items as $ad) {
          echo "<li><p>Ad [$ad_sn]: ".$ad->title.":</li>";
          echo '<img src="'.$ad->imgsrc.'" width="200" /></li>';
          $ad_sn++;
          echo "</p><br>";
        }
      ?>
   </ul>
  </body>
</html>
