import streamlit as st
import streamlit.components.v1 as components

# Define the HTML code
html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>706 Grey Wolves 7v7</title>
    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
        }
        .top-bar {
            position: sticky;
            top: 0;
            background-color: #333;
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 10px;
            z-index: 1000;
        }
        .top-bar img {
            height: 50px;
        }
        .nav-links {
            display: flex;
            list-style: none;
            padding: 0;
            margin: 0;
        }
        .nav-links li {
            margin: 0 15px;
        }
        .nav-links a {
            color: white;
            text-decoration: none;
            font-size: 16px;
        }
        .nav-links a:hover {
            text-decoration: underline;
        }
        .centered-text {
            text-align: center;
        }
        .carousel img {
            width: 100%;
            height: auto;
        }
        .columns {
            display: flex;
            justify-content: space-between;
        }
        .column {
            flex: 1;
            text-align: center;
        }
        h1, h2 {
            text-align: center;
        }
        section {
            margin: 40px 0;
        }
        html {
            scroll-padding-top: 80px;
        }
        #backToTopBtn {
        display: none; /* Hidden by default */
        position: fixed; /* Fixed/sticky position */
        bottom: 20px; /* Place the button at the bottom of the page */
        right: 30px; /* Place the button 30px from the right */
        z-index: 99; /* Make sure it does not overlap */
        border: none; /* Remove borders */
        outline: none; /* Remove outline */
        background-color: #555; /* Set a background color */
        color: white; /* Text color */
        cursor: pointer; /* Add a mouse pointer on hover */
        padding: 15px; /* Some padding */
        border-radius: 10px; /* Rounded corners */
        font-size: 18px; /* Increase font size */
        }
        #backToTopBtn:hover {
        background-color: #333; /* Add a dark-grey background on hover */
        }
        body {
        background-image: url('images/your-image.jpg'); /* Adjust the path based on your folder structure */
        background-attachment: fixed; /* This makes the background image stay fixed */
        background-size: cover; /* This ensures the image covers the entire background */
        background-repeat: no-repeat; /* Prevents the image from repeating */
        background-position: center; /* Centers the image */
        }
    </style>
</head>
<body>
    <div class="top-bar">
        <ul class="nav-links">
            <li><a href="#home">Home</a></li>
            <li><a href="#team-members">Team Members</a></li>
            <li><a href="#upcoming-matches">Upcoming Matches</a></li>
        </ul>
        <img src="https://raw.githubusercontent.com/marvinaviles85/706GreyWolves7v7/main/Images/706gw_no_bg.png" alt="Logo">
        <ul class="nav-links">
            <li><a href="#sponsorship-donations">Sponsorship and Donations</a></li>
            <li><a href="#registration">Registration</a></li>
            <li><a href="#apparel">Apparel</a></li>
            <li><a href="#contact-us">Contact Us</a></li>
        </ul>
    </div>

    <div id="content">
        <section id="home">
            <h1 class='title'>706 Grey Wolves 7v7</h1>
            <h1 class='centered-text'><strong>Welcome to the home of the 706 Grey Wolves!</strong><br><br>Explore our team members, schedule, and photos.</h1>
            <img src="Images/706gw_no_bg.png" style="width: 100%;">
            <h3 class='centered-text'>Registration is now open for age groups 11U to 18U! Spots are limited, so secure your place today!</h3>

            <div class="carousel">
                <img src="706GWImages/AllStars.jpg" alt="">
                <img src="706GWImages/BJ.jpg" alt="">
                <img src="706GWImages/BJ and Alan.jpg" alt="">
                <img src="706GWImages/cody.jpg" alt="">
                <img src="706GWImages/Dylan.jpg" alt="">
                <img src="706GWImages/FirstTeamImage.jpg" alt="">
                <img src="706GWImages/Flash.jpg" alt="">
                <img src="706GWImages/GetOutTheWay.jpg" alt="">
                <img src="706GWImages/HunterHeadTop.jpg" alt="">
                <img src="706GWImages/Isaac.jpg" alt="">
                <img src="706GWImages/MikeWeathers.jpg" alt="">
                <img src="706GWImages/MoneyInTheBank.jpg" alt="">
                <img src="706GWImages/PB12.jpg" alt="">
                <img src="706GWImages/TheBoys.jpg" alt="">
                <img src="706GWImages/TooStrong.jpg" alt="">
            </div>

            <h2>Latest News</h2>
            <p>Stay tuned for the latest news and updates.</p>

            <h1 class='centered-title'>Our Valued Sponsors</h1>
            <p class='subtext'>Click on the images to visit their websites</p>

            <div class="columns">
                <div class="column">
                    <div>
                        <a href="https://www.vetvalor.com" target="_blank">
                            <img src="https://raw.githubusercontent.com/marvinaviles85/706GreyWolves7v7/main/706GWImages/VetValor.PNG" width="200">
                        </a>
                    </div>
                </div>
                <div class="column" style="display: flex; justify-content: center; align-items: center; height: 100%;">
                    <a href="https://www.amsoil.com/?zo=408125" target="_blank">
                        <img src="https://raw.githubusercontent.com/marvinaviles85/706GreyWolves7v7/main/706GWImages/amsoil.png" width="200">
                    </a>
                </div>
                <div class="column" style="display: flex; justify-content: center; align-items: center; height: 100%;">
                    <a href="https://www.valleycenterrepair.com/" target="_blank">
                        <img src="https://raw.githubusercontent.com/marvinaviles85/706GreyWolves7v7/main/706GWImages/ValleyCenter.PNG" width="200">
                    </a>
                </div>
            </div>
        </section><br><br><br><br><br><br><br><br><br><br>

        <section id="team-members">
            <h1 class='centered-title'>706 Grey Wolves 7v7 Staff</h1>
            <div class="columns">
                <div class="column">
                    <img src="Images/MarvinSr.PNG" alt="Marvin Aviles" width="200">
                    <p>Position: Founder</p>
                    <img src="Images/MarvinJr.PNG" alt="Marvin Aviles Jr" width="200">
                    <p>Position: Defensive Coordinator</p>
                </div>
                <div class="column">
                    <img src="Images/Pam.jpg" alt="Pam Aviles" width="200">
                    <p>Position: Co-Founder/Team Trainer</p>
                </div>
            </div>
        </section>

        <section id="upcoming-matches">
            <h2>Upcoming Matches</h2>
            <ul>
                <li>2025-01-01 - vs TBD (TBD)</li>
                <li>2025-02-01 - vs TBD (TBD)</li>
                <!-- Add more matches here -->
            </ul>
        </section>

        <section id="sponsorship-donations">
            <h2>Donate or Sponsor the Grey Wolves</h2>
            <p>Support the 706 Grey Wolves by making a donation or becoming a sponsor. Your contribution helps cover the costs of uniforms, equipment, tournament fees, and more.</p>
            <div>
                <img src="Images/YourImageHere.png" alt="Sponsorship Image" style="width: 100%;">
            </div>
            <button onclick="showImpact()">What impact will your donation have?</button>
            <div id="impact-info" style="display: none;">
                <h3>Impact of Your Donation</h3>
                <p>
                    The 706 Grey Wolves (706 GW) is a dedicated travel 7v7 football team for youth aged 11-18. As we gear up for our second season with the Hands League, we are excited to announce our schedule from January 2025 to June 2025. Every Saturday, 706 GW will travel out of state for 7v7 tournaments, while also competing in local Augusta Hands League 7v7 tournaments. 706 GW thrives thanks to the generous support of our sponsors and the unwavering commitment of our volunteers. We invite you to join us in our mission to shape the leaders of tomorrow by supporting the 706 Grey Wolves.
                </p>
                <h4>Sponsorship Levels</h4>
                <ul>
                    <li><strong>$100 Individual Donation:</strong> Your business name and logo will be prominently displayed on our 706 Grey Wolves 7v7 website, Facebook page, and Instagram account.</li>
                    <li><strong>$250 Donation:</strong> Your business name and logo will be prominently featured on our 706 Grey Wolves 7v7 website, Facebook page, and Instagram account. Additionally, your logo will be included on a sponsor banner (provided by 706 GW) displayed every Saturday during multiple games.</li>
                    <li><strong>$500 Business Donation:</strong> Your business name and logo will be prominently displayed on our 706 Grey Wolves 7v7 website, Facebook page, and Instagram account. Additionally, your logo will be featured on a sponsor banner (provided by 706 GW) showcased every Saturday during multiple games, and proudly displayed on players’ uniforms.</li>
                </ul>
                <h4>Donation Information</h4>
                <p>Your generous donation assists with the costs of: uniforms, softshell helmets, player equipment, tournament fees, player insurance, qualified family assistance, and medical supplies.</p>
            </div>
            <script>
                function showImpact() {
                    var x = document.getElementById("impact-info");
                    if (x.style.display === "none") {
                        x.style.display = "block";
                    } else {
                        x.style.display = "none";
                    }
                }

                document.getElementById("payment-method").addEventListener("change", function() {
                    var paymentMethod = this.value;
                    document.getElementById("venmo-info").style.display = paymentMethod === "Venmo" ? "block" : "none";
                    document.getElementById("cashapp-info").style.display = paymentMethod === "CashApp" ? "block" : "none";
                });

                document.querySelectorAll('input[name="donation"]').forEach(function(elem) {
                    elem.addEventListener("change", function() {
                        var donationAmount = this.value === "One-time donation" ? document.getElementById("custom-amount").value : this.value;
                        document.getElementById("donation-amount").textContent = donationAmount;
                        document.getElementById("summary-donation-amount").textContent = donationAmount;
                    });
                });

                document.getElementById("custom-amount").addEventListener("input", function() {
                    var donationAmount = this.value;
                    document.getElementById("donation-amount").textContent = donationAmount;
                    document.getElementById("summary-donation-amount").textContent = donationAmount;
                });

                function submitDonation() {
                    var transactionId = document.getElementById("venmo-transaction-id").value || document.getElementById("cashapp-transaction-id").value;
                    var paymentMethod = document.getElementById("payment-method").value;

                    if (!transactionId) {
                        alert(`Please enter the ${paymentMethod} transaction ID to confirm your payment.`);
                    } else {
                        alert("Thank you for your donation!");
                        saveToCsv();
                    }
                }

                function saveToCsv() {
                    var email = document.getElementById("email").value;
                    var firstName = document.getElementById("first-name").value;
                    var lastName = document.getElementById("last-name").value;
                    var country = document.getElementById("country").value;
                    var state = document.getElementById("state").value;
                    var isCorporate = document.getElementById("corporate").checked;
                    var donationAmount = document.getElementById("donation-amount").textContent;
                    var paymentMethod = document.getElementById("payment-method").value;
                    var transactionId = document.getElementById("venmo-transaction-id").value || document.getElementById("cashapp-transaction-id").value;

                    var data = {
                        'Email': email,
                        'First Name': firstName,
                        'Last Name': lastName,
                        'Country': country,
                        'State': state,
                        'Corporate Donation': isCorporate,
                        'Donation Amount': donationAmount,
                        'Payment Method': paymentMethod,
                        'Transaction ID': transactionId
                    };

                    var csvFile = 'donations.csv';
                    var csvContent = "data:text/csv;charset=utf-8," 
                        + Object.keys(data).join(",") + "\n" 
                        + Object.values(data).join(",");

                    var encodedUri = encodeURI(csvContent);
                    var link = document.createElement("a");
                    link.setAttribute("href", encodedUri);
                    link.setAttribute("download", csvFile);
                    document.body.appendChild(link);
                    link.click();

                    uploadToGithub(csvFile);
                }

                function uploadToGithub(csvFile) {
                    var token = "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";
                    var repo = "706GreyWolves7v7";
                    var filePath = csvFile;

                    fetch(`https://api.github.com/repos/${repo}/contents/${filePath}`, {
                        method: 'PUT',
                        headers: {
                            'Authorization': `token ${token}`,
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify({
                            message: "Update donations",
                            content: btoa(csvContent)
                        })
                    }).then(response => response.json())
                      .then(data => console.log(data))
                      .catch(error => console.error('Error:', error));
                }
            </script>
        </section>

        <section id="registration">
            <h1 class='centered-title'>Register Now</h1>
            <div class="iframe-container">
                <iframe src="https://docs.google.com/forms/d/e/1FAIpQLSexO7RZIemrzcf0Y2pBDd1d7k8ehU7EqAJcwPVcXiW1ryCUjw/viewform?embedded=true" width="640" height="2665" frameborder="0" marginheight="0" marginwidth="0">Loading…</iframe>
            </div>
        </section>

        <section id="apparel">
            <h1>Apparel</h1>
            <iframe id="JotFormIFrame-242764337730156" title="Product Order Form" onload="window.parent.scrollTo(0,0)" allowtransparency="true" allow="geolocation; microphone; camera; fullscreen" src="https://form.jotform.com/242764337730156" frameborder="0" style="min-width:100%;height:2700px;border:none;overflow:auto;" scrolling="yes"></iframe>
            <script src='https://cdn.jotfor.ms/s/umd/latest/for-form-embed-handler.js'></script>
            <script>window.jotformEmbedHandler("iframe[id='JotFormIFrame-242764337730156']", "https://form.jotform.com/")</script>
        </section>

        <section id="contact-us">
            <h2>Contact Us</h2>
            <img src="Images/706gw_no_bg.png" style="width: 100%;">
            <p>Email us at <a href="mailto:706greywolves7v7@gmail.com">706greywolves7v7@gmail.com</a></p>
            <div style="text-align: center;">
                <a href="tel:+15207053812" style="
                    display: inline-block;
                    padding: 10px 20px;
                    font-size: 16px;
                    color: white;
                    background-color: #4CAF50;
                    border: none;
                    border-radius: 5px;
                    text-decoration: none;
                ">
                    1-520-705-3812
                </a>
            </div>
            <style>
                .social-icons img {
                    margin-right: 20px;
                }
            </style>
            <p><strong>Follow us on social media:</strong></p>
            <div class="social-icons">
                <a href="https://www.facebook.com/706GreyWolves7v7" target="_blank">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/5/51/Facebook_f_logo_%282019%29.svg" width="50" height="50">
                </a>
                <a href="https://www.instagram.com/706greywolves" target="_blank">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png" width="50" height="50">
                </a>
            </div>
        </section>
    </div>
    <button onclick="topFunction()" id="backToTopBtn" title="Go to top">Top</button>
    <script>
    // Get the button
    let mybutton = document.getElementById("backToTopBtn");

    // When the user scrolls down 20px from the top of the document, show the button
    window.onscroll = function() {scrollFunction()};

    function scrollFunction() {
        if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
            mybutton.style.display = "block";
        } else {
            mybutton.style.display = "none";
        }
    }

    // When the user clicks on the button, scroll to the top of the document
    function topFunction() {
        document.body.scrollTop = 0; // For Safari
        document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE, and Opera
    }
</script>

</body>
</html>
"""

# Use Streamlit components to render the HTML
components.html(html_code, height=800)
