import {
  regionList,
  regions,
  regionLocation,
  regionIndication,
} from "./region";

export function createDOM(properties: { level: number }) {
  const img = document.createElement("img");
  img.style.height = "32px";
  img.style.width = "32px";
  img.src = `https://r2-img.datavizu.app/level${properties.level}.png`;
  img.draggable = false;
  return img;
}

export const getCustomLayer = () => {
  return new BMapGL.CustomHtmlLayer(createDOM, {
    offsetX: 0,
    offsetY: 0,
    minZoom: 4,
    maxZoom: 15,
    enableDraggingMap: false,
  });
};

export const getCustomLayerData = (indication: string) => {
  const data: {
    type: string;
    features: {
      type: string;
      geometry: {
        type: string;
        coordinates: [number, number];
      };
      properties: {
        level: number;
      };
    }[];
  } = {
    type: "FeatureCollection",
    features: [],
  };
  regionList.forEach((region: string) => {
    const location = regionLocation[regions[region as keyof typeof regions]];
    data.features.push({
      type: "Feature",
      geometry: {
        type: "Point",
        coordinates: [location[0], location[1]],
      },
      properties: {
        level: Math.floor(
          (regionIndication[regions[region]][indication] * 5.99) / 5,
        ),
      },
    });
  });
  return data;
};

export const getLocationLayerData = () => {
  const data: {
    type: string;
    features: {
      type: string;
      geometry: {
        type: string;
        coordinates: [number, number];
      };
      properties: {
        level: number;
      };
    }[];
  } = {
    type: "FeatureCollection",
    features: [],
  };
  regionList.forEach((region: string) => {
    const location = regionLocation[regions[region as keyof typeof regions]];
    data.features.push({
      type: "Feature",
      geometry: {
        type: "Point",
        coordinates: [location[0], location[1]],
      },
      properties: {
        level: 3,
      },
    });
  });
  return data;
};
