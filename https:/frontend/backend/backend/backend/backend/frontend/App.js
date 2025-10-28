import React, { useState } from "react";
import { SafeAreaView, Text, TextInput, Button, StyleSheet, View } from "react-native";

export default function App() {
  const [input, setInput] = useState("");
  const [translated, setTranslated] = useState("");

  const handleTranslate = async () => {
    try {
      const response = await fetch("http://localhost:5000/ai/voice", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ lang: "bn", target: "en" }),
      });
      const data = await response.json();
      setInput(data.original || "");
      setTranslated(data.translated || "");
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <SafeAreaView style={styles.container}>
      <Text style={styles.title}>🎙️ Tynva Voice Translator</Text>
      <Button title="Speak & Translate" onPress={handleTranslate} />
      <View style={styles.resultBox}>
        <Text style={styles.label}>Original (বাংলা):</Text>
        <Text style={styles.text}>{input}</Text>
        <Text style={styles.label}>Translated (English):</Text>
        <Text style={styles.text}>{translated}</Text>
      </View>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, alignItems: "center", justifyContent: "center", padding: 20, backgroundColor: "#f2f2f2" },
  title: { fontSize: 24, fontWeight: "bold", marginBottom: 20 },
  resultBox: { marginTop: 20, width: "100%", padding: 10, backgroundColor: "#fff", borderRadius: 10 },
  label: { fontWeight: "600", marginTop: 10 },
  text: { fontSize: 16, color: "#333" },
});
