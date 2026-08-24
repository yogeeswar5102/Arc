from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>For Tamilselvi</title>

    <style>
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            min-height: 100vh;
            background: #0b0d12;
            color: #f5f5f5;
            font-family: Georgia, "Times New Roman", serif;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 16px 0;
            overflow-x: hidden;
            overflow-y: auto;
        }

        /* Background */

        .background {
            position: fixed;
            inset: 0;
            background:
                radial-gradient(
                    circle at 50% 35%,
                    rgba(130, 100, 150, 0.15),
                    transparent 40%
                ),
                linear-gradient(
                    135deg,
                    #08090d,
                    #11131b,
                    #090a0f
                );
            z-index: -2;
        }

        .stars {
            position: fixed;
            inset: 0;
            z-index: -1;
        }

        .star {
            position: absolute;
            width: 2px;
            height: 2px;
            background: white;
            border-radius: 50%;
            opacity: 0.3;
            animation: blink 4s infinite alternate;
        }

        @keyframes blink {
            from {
                opacity: 0.15;
            }
            to {
                opacity: 0.7;
            }
        }

        /* Main card */

        .card {
            width: 90%;
            max-width: 680px;
            padding: 48px 50px;
            text-align: center;

            background: rgba(255,255,255,0.035);
            border: 1px solid rgba(255,255,255,0.10);

            border-radius: 24px;

            backdrop-filter: blur(20px);

            box-shadow:
                0 30px 100px rgba(0,0,0,0.55);

            animation: appear 2s ease;
        }

        @keyframes appear {
            from {
                opacity: 0;
                transform: translateY(25px);
            }

            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .tiny {
            font-family: Arial, sans-serif;
            text-transform: uppercase;
            letter-spacing: 5px;
            font-size: 11px;
            color: #aaaab5;
            margin-bottom: 35px;
        }

        h1 {
            font-size: 52px;
            font-weight: normal;
            margin-bottom: 20px;
        }

        .line {
            width: 55px;
            height: 1px;
            background: #bca36a;
            margin: 30px auto;
        }

        .intro {
            font-family: Arial, sans-serif;
            font-size: 17px;
            line-height: 1.9;
            color: #c9c9d0;
        }

        button {
            margin-top: 38px;
            padding: 14px 32px;

            border-radius: 30px;

            border: 1px solid rgba(255,255,255,0.25);

            background: transparent;
            color: white;

            font-size: 15px;

            cursor: pointer;

            transition: all 0.35s ease;
        }

        button:hover {
            background: rgba(255,255,255,0.08);
            transform: translateY(-2px);
        }

        /* Message */

        #message {
            display: none;
            animation: appear 1.5s ease;
        }

        #message p {
            font-family: Arial, sans-serif;
            font-size: 17px;
            line-height: 2;
            color: #d4d4db;
            margin-bottom: 22px;
        }

        .highlight {
            color: #ffffff;
            font-size: 21px !important;
        }

        .signature {
            margin-top: 35px;
            font-family: Georgia, serif !important;
            font-size: 21px !important;
            color: #bca36a !important;
        }

        .heart {
            font-size: 30px;
            margin-bottom: 20px;
            opacity: 0.85;
        }

        .footer {
            margin-top: 45px;
            font-family: Arial, sans-serif;
            font-size: 11px;
            color: #777783;
            letter-spacing: 2px;
        }

        @media(max-width:600px) {

            .card {
                padding: 50px 25px;
            }

            h1 {
                font-size: 40px;
            }

            .intro,
            #message p {
                font-size: 16px;
            }
        }
    </style>
</head>

<body>

<div class="background"></div>

<div class="stars">
    <div class="star" style="top:10%;left:15%;"></div>
    <div class="star" style="top:20%;left:80%;"></div>
    <div class="star" style="top:35%;left:65%;"></div>
    <div class="star" style="top:75%;left:15%;"></div>
    <div class="star" style="top:85%;left:75%;"></div>
    <div class="star" style="top:50%;left:90%;"></div>
    <div class="star" style="top:15%;left:45%;"></div>
    <div class="star" style="top:65%;left:45%;"></div>
</div>


<div class="card">

    <!-- Opening -->

    <div id="opening">

        <div class="tiny">
            A little something for you
        </div>

        <h1>Tamilselvi</h1>

        <div class="line"></div>

        <p class="intro">
            I don't have a big speech.
            <br>
            I don't have anything to ask from you.
            <br><br>
            There is just something
            I wanted you to know.
        </p>

        <button onclick="openMessage()">
            Read this when you're ready
        </button>

    </div>


    <!-- Main Message -->

    <div id="message">

        <div class="heart">
            ♡
        </div>

        <h1>Tamilselvi</h1>

        <div class="line"></div>

        <p>
            I'm not here to ask you for anything.
        </p>

        <p class="highlight">
            I just wanted you to know that I'm here.
        </p>

        <p>
            I don't know what tomorrow will bring,
            and I don't want to force anything today.
        </p>

        <p>
            But if there is ever a moment when
            you feel like talking,
            laughing,
            sharing something,
            or simply having someone around...
        </p>

        <p class="highlight">
            I'll be here.
        </p>

        <p>
            No expectations.
            <br>
            No pressure.
            
        </p>

        <p>
            Just me,
            still wishing you well,
            still caring,
            and still here.
        </p>

        <p class="signature">
            — Yogeeswar
        </p>

        <div class="footer">
            SOME THINGS DON'T NEED TO BE RUSHED
        </div>

    </div>

</div>


<script>

function openMessage() {

    document.getElementById("opening").style.display = "none";

    document.getElementById("message").style.display = "block";

}

</script>

</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(HTML)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)