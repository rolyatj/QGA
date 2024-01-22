import SwiftUI

@main
struct GolfApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
    }
}

struct ContentView: View {
    var body: some View {
        ShotTrackerView()
    }
}