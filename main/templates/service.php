<?php
    include_once ("admin/classes/Database.php");
    $db = new classes\Database;
    $title = "Service";
    include ("inc/header_one.php");
?>
<!-- service section strart -->
<section id="service">
    <div class="container">
        <div class="service-content text-center">
            <h1 class="titleText text-dark">My Services</h1>
            <div class="row my-5">
                <?php
                    $select_srv = $db->select("SELECT * FROM `services`");
                    while($service = $select_srv->fetch_assoc()){
                ?>
                <div class="col-md-4 col-sm-6 my-4">
                    <div class="srvdiv">
                        <span class="d-block"><img src="<?= $dir.$service['image'] ?>" alt="Service icon"></span>
                        <h3 class="srv-title"><?= $service['name'] ?></h3>
                        <p><?= $service['srv_desc'] ?></p>
                    </div>
                </div>
                <?php } ?>
            </div>
            <button class="btn more-btn text-capitalize">view more</button>
        </div>
    </div>
    </section>
    <!-- service section end -->
<?php
    include ("inc/footer.php");
?>