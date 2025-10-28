import React, { useEffect, useRef, useState } from "react";
import { View, Button, Text, StyleSheet } from "react-native";
import { RTCView, mediaDevices } from "react-native-webrtc";
import io from "socket.io-client";

export default function CallScreen() {
  const socket = useRef(null);
  const [localStream, setLocalStream] = useState(null);
  const [remoteStream, setRemoteStream] = useState(null);

  useEffect(() => {
    socket.current = io("http://localhost:5001");

    mediaDevices.getUserMedia({ video: true, audio: true }).then(stream => {
      setLocalStream(stream);
    });

    return () => {
      if (socket.current) socket.current.disconnect();
    };
  }, []);

  return (
    <View style={styles.container}>
      <Text style={styles.title}>📞 Tynva Call Connected</Text>
      {localStream && <RTCView streamURL={localStream.toURL()} style={styles.video} />}
      {remoteStream && <RTCView streamURL={remoteStream.toURL()} style={styles.video} />}
      <Button title="End Call" color="red" onPress={() => console.log("Call ended")} />
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: "#000", justifyContent: "center", alignItems: "center" },
  title: { color: "#fff", fontSize: 20, marginBottom: 20 },
  video: { width: 300, height: 400, margin: 10, borderRadius: 10 },
});
