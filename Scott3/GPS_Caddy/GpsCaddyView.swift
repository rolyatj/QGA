
    import SwiftUI
    import MapKit

    struct GpsCaddyView: View {
        @State private var region = MKCoordinateRegion(
            center: CLLocationCoordinate2D(latitude: 34.011286, longitude: -116.166868),
            span: MKCoordinateSpan(latitudeDelta: 0.02, longitudeDelta: 0.02)
        )

        var body: some View {
            Map(coordinateRegion: $region)
        }
    }
    