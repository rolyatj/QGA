import SwiftUI
import ARKit

struct ShotTrackerView: View {
    var body: some View {
        ARViewContainer().edgesIgnoringSafeArea(.all)
    }
}

struct ARViewContainer: UIViewRepresentable {
    func makeUIView(context: Context) -> ARSCNView {
        let arView = ARSCNView(frame: .zero)
        // Configure ARView
        return arView
    }

    func updateUIView(_ uiView: ARSCNView, context: Context) {}
}