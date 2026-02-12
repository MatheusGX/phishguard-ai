async function scanURL() {

    const url = document.getElementById("urlInput").value;
    const resultContainer = document.getElementById("result");
    const classificationDiv = document.getElementById("classification");
    const riskBar = document.getElementById("riskBar");
    const scoreText = document.getElementById("scoreText");
    const featuresBox = document.getElementById("featuresBox");

    if (!url) return;

    resultContainer.classList.remove("hidden");
    classificationDiv.innerHTML = "🔍 A analisar...";
    classificationDiv.className = "text-gray-600 text-xl font-bold";

    riskBar.style.width = "0%";
    riskBar.classList.remove("bg-green-500", "bg-yellow-500", "bg-red-600");
    riskBar.classList.add("bg-gray-400");

    scoreText.innerHTML = "";
    featuresBox.innerHTML = "";

    try {
        const response = await fetch("/scan", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ url: url })
        });

        const data = await response.json();

        if (!response.ok) {
            classificationDiv.innerHTML = `❌ ${data.error}`;
            classificationDiv.className = "text-red-600 text-xl font-bold";
            return;
        }

        const score = data.score;
        const classification = data.classification;

        // Atualizar cor da barra
        riskBar.classList.remove("bg-gray-400");

        if (score >= 70) {
            riskBar.classList.add("bg-red-600");
            classificationDiv.className = "text-red-600 text-xl font-bold";
        } else if (score >= 40) {
            riskBar.classList.add("bg-yellow-500");
            classificationDiv.className = "text-yellow-600 text-xl font-bold";
        } else {
            riskBar.classList.add("bg-green-500");
            classificationDiv.className = "text-green-600 text-xl font-bold";
        }

        classificationDiv.innerHTML = `Classificação: ${classification}`;

        riskBar.style.transition = "width 0.8s ease-in-out";
        riskBar.style.width = score + "%";

        scoreText.innerHTML = `Risk Score: ${score}%`;

        // Features
        let featuresHTML = "<strong>Detalhes Técnicos:</strong><ul class='list-disc pl-5 mt-2'>";
        for (const key in data.features) {
            featuresHTML += `<li>${key}: ${data.features[key]}</li>`;
        }
        featuresHTML += "</ul>";

        featuresBox.innerHTML = featuresHTML;

    } catch (error) {
        classificationDiv.innerHTML = "❌ Erro ao comunicar com o servidor.";
        classificationDiv.className = "text-red-600 text-xl font-bold";
    }
}
