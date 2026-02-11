async function scanURL() {
    const url = document.getElementById("urlInput").value;
    const resultDiv = document.getElementById("result");

    if (!url) {
        resultDiv.innerHTML = "⚠️ Introduza uma URL válida.";
        resultDiv.className = "mt-6 text-center text-lg font-semibold text-yellow-600";
        return;
    }

    resultDiv.innerHTML = "🔍 A analisar...";
    resultDiv.className = "mt-6 text-center text-lg font-semibold text-gray-600";

    try {
        const response = await fetch("/scan", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ url: url })
        });

        const data = await response.json();

        let colorClass = "text-green-600";

        if (data.classification === "Phishing") {
            colorClass = "text-red-600";
        } else if (data.classification === "Suspicious") {
            colorClass = "text-yellow-600";
        }

        resultDiv.className = `mt-6 text-center text-lg font-semibold ${colorClass}`;

        resultDiv.innerHTML = `
            Classificação: ${data.classification}<br>
            Risk Score: ${data.score}
        `;

    } catch (error) {
        resultDiv.innerHTML = "❌ Erro ao comunicar com o servidor.";
        resultDiv.className = "mt-6 text-center text-lg font-semibold text-red-600";
    }
}
